import asyncio

from service.push import message_sender


async def main():
    await message_sender.start_sending()


if __name__ == '__main__':
    asyncio.run(main())
