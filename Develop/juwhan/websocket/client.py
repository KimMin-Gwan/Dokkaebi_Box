import asyncio
import websockets

async def connect_to_server():
    async with websockets.connect('ws://localhost:9998') as websocket:
        while True:
            message = input("Enter a message: ")
            await websocket.send(message)
            response = await websocket.recv()
            print("Server response: " + response)

if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(connect_to_server())