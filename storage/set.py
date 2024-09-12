from storage.connection import RedisConnection
from storage.settings.cluster import ClusterConfig


class RedisSetData:
    EXPIRE_TIMEOUT = ClusterConfig.EXPIRE_TIMEOUT

    def __init__(
            self, connection: RedisConnection.redis
    ) -> None:
        self.connection = connection

    async def is_exists(self, key: str) -> bool:
        return True if await self.connection.exists(key) else False

    async def is_unique(self, key: str, message: str) -> bool:
        value = await self.connection.get(key)
        return True if value.decode('utf-8') != message else False

    async def set_data(
            self, key: str, value: str, expire_flag: bool = False
    ) -> None:
        if await self.is_exists(key=key):
            if await self.is_unique(key=key, message=value):
                await self.connection.set(key, value)
                if expire_flag:
                    await self.connection.expire(key, self.EXPIRE_TIMEOUT)
        else:
            await self.connection.set(key, value)
