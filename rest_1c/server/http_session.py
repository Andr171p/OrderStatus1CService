import aiohttp

from loguru import logger

from rest_1c.settings.config import RequestHeaders, RequestLoggingMessage


class HTTPSession(RequestHeaders):

    @staticmethod
    def is_ok(response) -> bool:
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
                        logger.info(RequestLoggingMessage.successful_response)
                        return result
        except Exception as _ex:
            logger.warning(_ex)
