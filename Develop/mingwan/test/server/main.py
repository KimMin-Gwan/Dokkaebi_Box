from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()

# 메시지를 저장할 리스트 초기화
messages = []

class Message(BaseModel):
    content: str

# 새 메시지를 저장하는 엔드포인트
@app.post("/messages/", response_model=Message)
def create_message(message: Message):
    print(message)
    messages.append(message.content)
    return message

# 저장된 모든 메시지를 반환하는 엔드포인트
@app.get("/messages/", response_model=List[Message])
def get_messages():
    return [{"content": message} for message in messages]
