from fastapi import FastAPI
from View import AppServer
from Controller import Web_Controller
from Model import *
from Model.DBMS import *
class Main:
    def __init__(self):
        self.app = FastAPI()
        self.dbms= DataBase()
        self.model=Model(self.dbms)
        self.web_controller = Web_Controller(self.model)
        self.app_server = AppServer(self.app, self.web_controller)

def main():
    main_cls = Main()
    import uvicorn
    uvicorn.run(main_cls.app_server, host="127.0.0.1", port=8000)


if __name__ == "__main__":
    main()