from fastapi import FastAPI
from View import AppServer
from Controller import Web_Controller
from Model import *
from Model.DBMS import *
from fastapi.responses import FileResponse
class Main:
    def __init__(self):
        self.app = FastAPI()
        self.dbms= DataBase()
        self.model=Model(self.dbms)
        self.web_controller = Web_Controller(self.model)
        #self.app_server = AppServer(self.app, self.web_controller)
        self.sample()
        
        
    def sample(self):
        @self.app.get('/')
        async def ma():
            return {"message":"hello"}
        @self.app.get('/find')
        async def return_data():
            result = self.web_controller.find()  #사진 path가 return된다. 
            return FileResponse(result,media_type="image/jpeg")  #file_Response를 통해서사진 출력
            #실제로는 result는 사진 데이터? 가 와야함 
        
        
def main():
    main_cls = Main()
    import uvicorn
    uvicorn.run(main_cls.app, host="127.0.0.1", port=8000)


if __name__ == "__main__":
    main()