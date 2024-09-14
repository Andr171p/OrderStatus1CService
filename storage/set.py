from storage.connection import RedisConnection
from storage.settings.cluster import ClusterConfig

from misc.time_utils import timestamp


class RedisSetData:
    EXPIRE_TIMEOUT = ClusterConfig.EXPIRE_TIMEOUT

    def __init__(
            self, connection: RedisConnection.redis
    ) -> None:
        self.connection = connection

    async def is_exists(self, key: str) -> bool:
        return True if await self.connection.exists(key) else False

    async def is_unique(self, key: str, message: str) -> bool:
        value = await self.connection.hget(key, "value")
        print(value.decode('utf-8'))
        return True if value.decode('utf-8') != message else False

    async def set_data(
            self, key: str, value: str, expire_flag: bool = False
    ) -> None:
        if await self.is_exists(key=key):
            print("key exists")
            if await self.is_unique(key=key, message=value):
                print("value is unique")
                # await self.connection.set(key, value)
                print(f"value: {value}")
                await self.connection.delete(key)
                await self.connection.hset(
                    name=key,
                    mapping={
                        "value": value,
                        "timestamp": timestamp()
                    }
                )
                print("+")
                if expire_flag:
                    await self.connection.expire(key, self.EXPIRE_TIMEOUT)
            else:
                print("value exists")
        else:
            # await self.connection.set(key, value)
            await self.connection.hset(
                key,
                mapping={
                    "value": value,
                    "timestamp": timestamp()
                }
            )
