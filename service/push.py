from storage.connection import RedisConnection
from storage.set import RedisSetData

from misc.tamplates import MessageTemplate


class PushMessage:
    connection = RedisConnection()
    redis = None

    @classmethod
    async def connect(cls) -> RedisSetData:
        redis = await cls.connection.connect()
        cls.redis = RedisSetData(connection=redis)
        return cls.redis

    @classmethod
    async def push(cls, data: dict) -> None:
        cls.redis = await cls.connect()
        message = MessageTemplate(order=data).message()
        print(message)
        await cls.redis.set_data(
            key=message['number'],
            value=message['message']
        )


pusher = PushMessage()
