import json

import logging

from service_1c.config import RequestLoggingMessage


request_logging = RequestLoggingMessage()
logging.basicConfig(level=logging.INFO)


def extract_orders_data(response):
    if response is not None:
        _json = json.dumps(response, ensure_ascii=False)
        _dict = json.loads(_json)
        orders = _dict['data']['orders']
        logging.info(orders)
        return orders
    else:
        logging.warning(request_logging.none_json_response)
        return -1
