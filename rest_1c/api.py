from rest_1c.server.http_session import HTTPSession
from rest_1c.settings.config import RequestData, RequestHeaders
from rest_1c.schemas import request_models
from rest_1c.utils import (
    extract_orders_data,
    extract_flyers_data
)

from misc.format_data import format_telefon

from typing import List


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
        response = await self.post_request(data=data.model_dump())
        return response

    async def orders(self) -> List[dict]:
        data = {
            'command': f'{self.request_data.orders}',
            'active': 'true'
        }
        data = request_models.OrdersModel.model_validate(data)
        response = await self.post_request(data=data.model_dump())
        orders = extract_orders_data(json_=response)
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
        return flyers

    async def history(self, telefon: str) -> dict:
        telefon = format_telefon(telefon=telefon)
        data = {
            'command': f'{self.request_data.history}',
            'telefon': f'{telefon}',
            'project': f'{self.request_headers.project}'
        }
        data = request_models.HistoryModel.model_validate(data)
        response = await self.post_request(data=data.model_dump())
        return response


status_api = StatusAPI()
import asyncio

r = asyncio.run(status_api.flyers(telefon='89829764729'))
print(r)