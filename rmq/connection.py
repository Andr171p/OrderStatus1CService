import pika

from rmq.settings.server_config import ConnectData
from rmq.settings.queue_config import QueueConfig


class RMQConnection:
    connection = pika.BlockingConnection(
        pika.URLParameters(ConnectData.RMQ_URL)
    )
    channel = connection.channel()

    @staticmethod
    def create_queue(channel):
        channel.queue_declare(QueueConfig.queue_name)

