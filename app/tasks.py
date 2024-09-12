from rest_1c.api import status_api
from rest_1c.utils import is_empty

from service.push import pusher

import logging


logging.basicConfig(level=logging.INFO)


async def get_status() -> None:
    orders = await status_api.orders()
    logging.info(orders)
    if not is_empty(data=orders):
        for order in orders:
            await pusher.push(data=order)
