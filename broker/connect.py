import pika

from broker.config import ConnectData
from broker.config import SettingsBroker


class BrokerConnection:
    connection = pika.BlockingConnection(
        pika.URLParameters(ConnectData.URL)
    )
    channel = connection.channel()
    channel.queue_declare(SettingsBroker.queue_name)
