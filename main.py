import asyncio

from app.worker import work


async def main() -> None:
    await work()


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
