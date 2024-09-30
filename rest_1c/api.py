from rest_1c.server.http_session import HTTPSession
from rest_1c.settings.config import RequestData, RequestHeaders
from rest_1c.schemas import request_models
from rest_1c.utils import (
    extract_orders_data,
    extract_flyers_data
)

from misc.format_data import format_telefon

from typing import List

from loguru import logger


class StatusAPI(HTTPSession):
    def __init__(self):
        self.request_headers = RequestHeaders()
        self.request_data = RequestData()

    async def order(self, telefon: str) -> List[dict]:
        telefon = format_telefon(telefon=telefon)
        data = {
            'command': f'{self.request_data.order}',
            'telefon': f'{telefon}'
        }
        data = request_models.OrderModel.model_validate(data)
        order = await self.post_request(data=data.model_dump())
        logger.info(order)
        return order

    async def orders(self) -> List[dict]:
        data = {
            'command': f'{self.request_data.orders}',
            'active': 'true'
        }
        data = request_models.OrdersModel.model_validate(data)
        response = await self.post_request(data=data.model_dump())
        orders = extract_orders_data(json_=response)
        logger.info(orders)
        return orders

    async def flyers(self, telefon: str) -> dict:
        telefon = format_telefon(telefon=telefon)
        data = {
            'command': f'{self.request_data.flyer}',
            'telefon': f'{telefon}',
            'project': f'{self.request_headers.project}'
        }
        data = request_models.FlyerModel.model_validate(data)
        response = await self.post_request(data=data.model_dump())
        flyers = extract_flyers_data(json_=response)
        logger.info(flyers)
        return flyers

    async def history(self, telefon: str) -> dict:
        telefon = format_telefon(telefon=telefon)
        data = {
            'command': f'{self.request_data.history}',
            'telefon': f'{telefon}',
            'project': f'{self.request_headers.project}'
        }
        data = request_models.HistoryModel.model_validate(data)
        history = await self.post_request(data=data.model_dump())
        logger.info(history)
        return history


status_api = StatusAPI()