from fastapi import FastAPI, HTTPException 
from fastapi.responses import RedirectResponse
from package import Model


class AppServer():
    # 초기화
    def __init__(self, app, controller):
        # app 동기화
        self.app = app
        self.controller = controller # 웹페이지
        self.register_routes()

    def register_routes(self):
        # 홈화면
        @self.app.get('/')
        def main_view(self):
            result = self.controller.mainpage() # div 박스가 리턴되어야함
            return result

        # 맡기기
        # 본인인증이 필요함
        @self.app.get('/hand_over/{device_id}/{client_id}/{temp_id}')
        async def read_item(device_id: int, client_id : int, temp_id : int):
            # 유효성 검사를 실시
            result = self.controller.hand_over(device_id, client_id, temp_id)
            if self.exception_control(result):
                return RedirectResponse("/bad_request")
            return result
        
        # 되찾기
        # 본인인증이 필요함
        


        
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










