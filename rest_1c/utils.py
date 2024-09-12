import json

import logging

from rest_1c.settings.config import RequestLoggingMessage


request_logging = RequestLoggingMessage()
logging.basicConfig(level=logging.INFO)


def extract_orders_data(json_):
    if json_ is not None:
        _json = json.dumps(json_, ensure_ascii=False)
        _dict = json.loads(_json)
        orders = _dict['data']['orders']
        logging.info(orders)
        return orders
    else:
        logging.warning(request_logging.none_json_response)
        return -1


def extract_flyers_data(json_):
    if json_ is not None:
        _json = json.dumps(json_, ensure_ascii=False)
        _dict = json.loads(_json)
        flyers = _dict['data']
        logging.info(flyers)
        return flyers
    else:
        return -1


def is_empty(data: list) -> bool:
    return True if len(data) == 0 else False
