from fastapi import FastAPI, HTTPException, WebSocket
from pydantic import BaseModel
#import websockets
from starlette.middleware.cors import CORSMiddleware
from fastapi.websockets import WebSocketDisconnect

app = FastAPI()

# 메시지를 저장하기 위한 임시 데이터 구조
chat_history = []

class Message(BaseModel):
    text: str

# CORS 미들웨어 설정 (Cross-Origin Resource Sharing)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 원격 호스트의 웹소켓 연결을 허용할 도메인 설정
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# WebSocket 연결을 다루는 핸들러 함수
#@app.websocket("/")
#async def websocket_endpoint(websocket: WebSocket):
    #await websocket.accept()
    #while True:
        #try:
            #message = await websocket.receive_text()
        #except Exception as e:
            #pass
            ##print("WebSocket receive_text error:", str(e))
        ##message = await websocket.receive_text()
        ##text = type(message)
        #print(message)
        ##print(text)
        #text = "Im server"
        #await websocket.send_text(text)
        #print(text)

# WebSocket 연결을 다루는 핸들러 함수
@app.websocket("/")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    while True:
        message = await websocket.receive_text()
        print(message)
        await websocket.send_text("서버에서 보낸 메시지: " + message)  # 서버에서 메시지 전송



#@app.websocket("/")
#async def websocket_endpoint(websocket: WebSocket):
    #await websocket.accept()
    #try:
        #while True:
            #message = await websocket.receive_text()
            ## 웹소켓 연결이 종료되었을 때 메시지 전송을 중단
            #if not websocket.client_state:
                #break
            #print(message)
            #await websocket.send_text("from server " + message)
    #except WebSocketDisconnect:
        #print("WebSocket connection closed.")

@app.get("/api/chat/history")
def get_chat_history():
    return chat_history

@app.post("/api/chat/send")
def send_message(message: Message):
    chat_history.append(message)
    print(message.text)
    return {"message": "메시지가 성공적으로 전송되었습니다."}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)

#118.41.235.154