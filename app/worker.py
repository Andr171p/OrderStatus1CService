from app.session import Periodic
from app.tasks import get_status
from app.config import TaskConfig

from loguru import logger

import asyncio


async def start() -> None:
    periodic = Periodic(
        func=get_status,
        timeout=TaskConfig.TIME_INTERVAL_PER_SECS
    )
    try:
        logger.info("SERVICE WAS STARTED...")
        await periodic.start()
    except Exception as _ex:
        logger.info("SERVICE ERROR")
        logger.warning(_ex)
        await periodic.stop()
    finally:
        await periodic.stop()
        logger.info("SERVICE WAS STOPPED...")
        logger.info(f"SERVICE ERROR WAITING TIMEOUT: {TaskConfig.SERVICE_ERROR_TIMEOUT}")
        await asyncio.sleep(TaskConfig.SERVICE_ERROR_TIMEOUT)
        logger.info("SERVICE RESTART...")
        await start()
