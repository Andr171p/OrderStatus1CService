import aiohttp

import logging

from rest_1c.settings.config import RequestHeaders, RequestLoggingMessage


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
