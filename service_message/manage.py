import asyncio

import logging

from service_1c.api import Statuses

from service_message.params import TriggerStatuses, SettingsSender
from service_message.tamplates import MessageTemplate

from rmq.publisher import BrokerSendMessage


logging.basicConfig(level=logging.INFO)


class MessageSender:
    def __init__(self):
        self.broker = BrokerSendMessage()
        self.statuses = Statuses()

        self.old_data = None
        self.new_data = None

    async def send_message(self, message):
        self.broker.publish(message=message)

    @staticmethod
    def update(old_data, new_data):
        triggers = TriggerStatuses.statuses
        result = []
        for order in new_data:
            if order not in old_data and order['status'] in triggers:
                result.append(order)
        logging.info(f"NEW ORDERS:\n{result}")
        return result

    async def broadcast(self, data):
        for order in data:
            message = MessageTemplate(order=order).message()
            await self.send_message(message=message)

    async def start_sending(self):
        self.old_data = await self.statuses.orders_response()
        while True:
            await asyncio.sleep(SettingsSender.timeout)
            self.new_data = await self.statuses.orders_response()
            result = self.update(
                old_data=self.old_data,
                new_data=self.new_data
            )
            if len(result) != 0:
                await self.broadcast(data=result)

            self.old_data = self.new_data


message_sender = MessageSender()
