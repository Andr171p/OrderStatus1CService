import asyncio

from service_1c.statuses import Statuses

from service_message.params import TriggerStatuses


class MessageSender:
    async def send_message(self):
        pass

    @staticmethod
    def update(old_data, new_data):
        triggers = TriggerStatuses.statuses
        result = []
        for order in new_data:
            if order not in old_data and order['status'] in triggers:
                result.append(order)
        return result
