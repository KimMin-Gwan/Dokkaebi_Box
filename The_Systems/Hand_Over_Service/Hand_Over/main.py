from view import AppServer
from fastapi import FastAPI
from DBMS import *
from controller import *
import uvicorn

class Info:
    def __init__(self):
        self.img_num=0
        
    def get_img_num(self):
        return self.img_num
    
    def set_img_num(self):
        self.img_num+=1
    
def main():
    app = FastAPI()
    info = Info()
    model = DataBase()
    controller = Web_Controller(model, info)
    appserver = AppServer(app, controller)
    uvicorn.run(app, host="127.0.0.1", port=8000)


if __name__ == "__main__":
    main()