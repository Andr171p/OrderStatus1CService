from storage.connection import RedisConnection
from storage.settings.cluster import ClusterConfig


class RedisSetData:
    EXPIRE_TIMEOUT = ClusterConfig.EXPIRE_TIMEOUT

    def __init__(
            self, connection: RedisConnection.redis
    ) -> None:
        self.connection = connection

    async def set_data(
            self, key: str, value: str, expire_flag: bool = False
    ) -> None:
        await self.connection.set(key, value)
        if expire_flag:
            await self.connection.expire(key, self.EXPIRE_TIMEOUT)
