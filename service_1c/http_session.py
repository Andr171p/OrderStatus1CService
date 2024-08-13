import aiohttp

import asyncio

import logging

from service_1c.config import RequestHeaders, RequestLoggingMessage, RequestData


class HTTPSession(RequestHeaders):
    logging.basicConfig(level=logging.INFO)

    @staticmethod
    def is_ok(response):
        status = response.status
        if status == 200:
            return True
        else:
            return False

    async def post_request(self, data):
        try:
            async with aiohttp.ClientSession() as session:
                async with session.post(
                        url=self.url,
                        headers=self.headers,
                        json=data,
                        timeout=self.timeout
                ) as response:
                    if self.is_ok(response=response):
                        result = await response.json()
                        logging.info(RequestLoggingMessage.successful_response)
                        return result
        except Exception as _ex:
            logging.warning(_ex)


ht = HTTPSession()
d = {'command': RequestData.orders,
     'active': 'true'}
r = asyncio.run(ht.post_request(data=d))
print(r)
