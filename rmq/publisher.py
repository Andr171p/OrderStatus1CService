from rmq.settings.queue_config import queue_config
from rmq.connection import RMQConnection

import logging


class RMQSendMessage(RMQConnection):
    logging.basicConfig(level=logging.INFO)

    def publish(self, message):
        self.channel.basic_publish(
            exchange='',
            routing_key=queue_config.queue_name,
            body=message
        )
        logging.info(f"[{queue_config.queue_name}] SENT: {message}")
        # self.connection.close()
