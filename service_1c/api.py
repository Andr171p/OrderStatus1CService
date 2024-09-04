from service_1c.server.http_session import HTTPSession
from service_1c.settings.config import RequestData, RequestHeaders
from service_1c.schemas import request_models
from service_1c.utils import extract_orders_data

from misc.format_data import format_telefon


class Statuses(HTTPSession):
    def __init__(self):
        self.request_headers = RequestHeaders()
        self.request_data = RequestData()

    async def order_response(self, telefon: str):
        telefon = format_telefon(telefon=telefon)
        data = {
            'command': f'{self.request_data.order}',
            'telefon': f'{telefon}'
        }
        data = request_models.OrderModel.model_validate(data)
        response = await self.post_request(data=data.model_dump())
        return response

    async def orders_response(self):
        data = {
            'command': f'{self.request_data.orders}',
            'active': 'true'
        }
        data = request_models.OrdersModel.model_validate(data)
        response = await self.post_request(data=data.model_dump())
        result = extract_orders_data(response=response)
        return result

    async def flyer_response(self, telefon: str):
        telefon = format_telefon(telefon=telefon)
        data = {
            'command': f'{self.request_data.flyer}',
            'telefon': f'{telefon}',
            'project': f'{self.request_headers.project}'
        }
        data = request_models.FlyerModel.model_validate(data)
        response = await self.post_request(data=data.model_dump())
        return response

    async def history_response(self, telefon: str):
        telefon = format_telefon(telefon=telefon)
        data = {
            'command': f'{self.request_data.history}',
            'telefon': f'{telefon}',
            'project': f'{self.request_headers.project}'
        }
        data = request_models.HistoryModel.model_validate(data)
        response = await self.post_request(data=data.model_dump())
        return response
