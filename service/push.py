from storage.connection import RedisConnection
from storage.set import RedisSetData

from misc.tamplates import MessageTemplate


class PushMessage:
    connection = RedisConnection()
    redis = RedisSetData(connection=connection)

    @classmethod
    async def push(cls, data: dict) -> None:
        message = MessageTemplate(order=data).message()
        await cls.redis.set_data(
            key=message['number'],
            value=message['message']
        )


pusher = PushMessage()
