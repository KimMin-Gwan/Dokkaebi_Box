from fastapi.responses import RedirectResponse
from fastapi.responses import FileResponse
from fastapi import FastAPI, HTTPException, WebSocket
from pydantic import BaseModel
from starlette.middleware.cors import CORSMiddleware
from fastapi.websockets import WebSocketDisconnect
from ChatBot.ChatBotData import *
import base64

class AppServer():
    # 초기화
    def __init__(self, app, controller):
        # app 동기화
        self.app = app
        self.controller = controller # 웹페이지
        # CORS 미들웨어 설정 (Cross-Origin Resource Sharing)
        self.app.add_middleware(
            CORSMiddleware,
            allow_origins=["*"],  # 원격 호스트의 웹소켓 연결을 허용할 도메인 설정
            allow_credentials=True,
            allow_methods=["*"],
            allow_headers=["*"],
        )
        self.register_routes()

    def register_routes(self):
        # 홈화면
        @self.app.get('/')
        async def main_view(self):
            #result = self.controller.mainpage() # div 박스가 리턴되어야함
            #return result
            return {"message":"기본 웹페이지 입니다."}
        # WebSocket 연결을 다루는 핸들러 함수

        @self.app.websocket("/")
        async def websocket_endpoint(websocket: WebSocket):
            self.bot = self.controller.get_bot()  #사진 path가 return된다. 
            await websocket.accept()
            message = await websocket.receive_text()

            flag = True
            while (flag):
                res, flag = self.bot.fun1(message)
                await websocket.send_text(res)  # 서버에서 메시지 전송

                message = await websocket.receive_text()
            flag = True
            while (flag):
                res, flag = self.bot.fun2(message)
                await websocket.send_text(res)  # 서버에서 메시지 전송

                message = await websocket.receive_text()

            flag = True

            while (flag):
                res, flag = self.bot.fun3(message)
                await websocket.send_text(res)  # 서버에서 메시지 전송

                message = await websocket.receive_text()

            flag = True
            while (flag):
                res, flag = self.bot.fun4()
                await websocket.send_text(res)

            self.controller.find_data_from_bot()
        
        # 되찾기
        # 본인인증이 필요함
        #@self.app.get('/find')
        #async def return_data():
            #result = self.controller.find()  #사진 path가 return된다. 
            #if result !=False:
                #return FileResponse(result,media_type="image/jpeg")  #file_Response를 통해서사진 출력
            ##실제로는 result는 사진 데이터? 가 와야함 
            #else:
                #return {"messages":"찾는 데이터가 없음 에 따른 출력 ...추후 구현"}

        # 되찾기
        # 본인인증이 필요함

        # 본인인증이 필요함
        @self.app.get('/getImage')
        async def return_data():
            path = self.controller.get_image_data()
            with open(path, "rb") as image_file:
                image_data = base64.b64encode(image_file.read()).decode('utf-8')
            
            return {"image_data": image_data}

        @self.app.get('/getItem')
        async def return_data():
            result = self.controller.get_item_data()
            return result
        
        # 잘못된 진입 처리
        @self.app.get('/bad_request')
        async def bad_request(resquest, exc):
            result = self.bad_result()
            return result
        
        # 예외처리
        @self.app.exception_handler(HTTPException)
        async def custom_exception_handler(request, exc):
            if exc.status_code == 403:
                return RedirectResponse("/bad_request")
            return await self.super().custom_exception_handler(request, exc)
        

    # 예외상황 처리
    def exception_control(self, result):
        # 유효하지 않으면 True 
        if result['flag'] == True:
            True
        else:
            False
        
    def bad_result(self):
        pass
    

