import asyncio

from service_message.manage import MessageSender


message_sender = MessageSender()


async def main():
    await message_sender.start_sending()


if __name__ == '__main__':
    asyncio.run(main())
