from app.session import Periodic
from app.tasks import get_status
from app.config import TaskConfig

import logging


logging.basicConfig(level=logging.INFO)


async def work() -> None:
    periodic = Periodic(
        func=await get_status(),
        timeout=TaskConfig.TIME_INTERVAL_PER_SECS
    )
    try:
        logging.info("APP WAS STARTED...")
        await periodic.start()
    except Exception as _ex:
        logging.info("APP ERROR")
        logging.warning(_ex)
        await periodic.stop()
    finally:
        await periodic.stop()
        logging.info("APP WAS STOPPED...")
