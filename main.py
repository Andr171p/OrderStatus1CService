import asyncio
import websockets
import json


async def send_request():
    uri = "wss://noname-sushi.online/web/hs/hook?token=NTAxNGVhNWMtZTUwYi00NTdjLTk5NTctNmIyMmM2N2U5NzRh"
    async with websockets.connect(uri) as websocket:
        data = {
            "command": "status",
            "telefon": "+7(950)484-79-54"
        }
        await websocket.send(json.dumps(data))
        response = await websocket.recv()
        print(response)


asyncio.get_event_loop().run_until_complete(send_request())
