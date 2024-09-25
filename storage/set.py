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
        return True if value.decode('utf-8') != message else False

    async def mapping(
            self, key: str, value: str, telefon: str, pay_link: str, project: str, status: str
    ) -> None:
        await self.connection.hset(
            name=key,
            mapping={
                "value": value,
                "timestamp": timestamp(),
                "telefon": telefon,
                "pay_link": pay_link,
                "project": project,
                "status": status
            }
        )

    async def set_data(
            self, key: str, value: str, telefon: str, pay_link: str, project: str, status: str
    ) -> None:
        if await self.is_exists(key=key):
            if await self.is_unique(key=key, message=value):
                await self.connection.delete(key)
                await self.mapping(key, value, telefon, pay_link, project, status)
            else:
                pass
        else:
            await self.mapping(key, value, telefon, pay_link, project, status)
