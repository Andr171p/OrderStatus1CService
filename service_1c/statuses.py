from service_1c.http_session import HTTPSession
from service_1c.config import RequestData, RequestHeaders
from service_1c import models


class Statuses(HTTPSession):
    def __init__(self):
        self.request_headers = RequestHeaders()
        self.request_data = RequestData()

    async def order_response(self, telefon: str):
        data = {
            'command': f'{self.request_data.order}',
            'telefon': f'{telefon}'
        }
        data = models.OrderModel.model_validate(data)
        response = await self.post_request(data=data.model_dump())
        return response

    async def orders_response(self):
        data = {
            'command': f'{self.request_data.orders}',
            'active': 'true'
        }
        data = models.OrdersModel.model_validate(data)
        response = await self.post_request(data=data.model_dump())
        return response

    async def flyer_response(self, telefon: str):
        data = {
            'command': f'{self.request_data.flyer}',
            'telefon': f'{telefon}',
            'project': f'{self.request_headers.project}'
        }
        data = models.FlyerModel.model_validate(data)
        response = await self.post_request(data=data.model_dump())
        return response

    async def history_response(self, telefon: str):
        data = {
            'command': f'{self.request_data.history}',
            'telefon': f'{telefon}',
            'project': f'{self.request_headers.project}'
        }
        data = models.HistoryModel.model_validate(data)
        response = await self.post_request(data=data.model_dump())
        return response
