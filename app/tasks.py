from rest_1c.api import status_api
from rest_1c.utils import is_empty

from service.push import pusher

from loguru import logger


async def get_status() -> None:
    orders = await status_api.orders()
    logger.info(orders)
    if not is_empty(data=orders):
        for order in orders:
            logger.info(f"NUMBER OF ORDER: {order['number']}")
            await pusher.push(data=order)
