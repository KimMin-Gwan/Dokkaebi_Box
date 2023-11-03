import asyncio
import websockets

async def chat_server(websocket, path):
    try:
        async for message in websocket:
            # 클라이언트로부터 메시지 수신
            print(f"Received: {message}")

            # 메시지를 다시 클라이언트에게 전송
            await websocket.send(message)
    except websockets.exceptions.ConnectionClosedOK:
        print("Client disconnected")

start_server = websockets.serve(chat_server, "localhost", 8765)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()