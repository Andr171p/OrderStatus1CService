from broker.config import SettingsBroker
from broker.connect import BrokerConnection

import logging


class BrokerSendMessage(BrokerConnection):
    logging.basicConfig(level=logging.INFO)

    def publish(self, message):
        self.channel.basic_publish(
            exchange='',
            routing_key=SettingsBroker.queue_name,
            body=message
        )
        logging.info(f"[x] SENT: {message}")
        # self.connection.close()
