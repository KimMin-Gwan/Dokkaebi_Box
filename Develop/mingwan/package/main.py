from fastapi import FastAPI
from View import AppServer
from Controller import Web_Controller
from Model.DBMS import Databass


class Main:
    def __init__(self):
        self.app = FastAPI()
        self.web_controller = Web_Controller()
        self.app_server = AppServer(self.app, self.web_controller)



def main():
    main_cls = Main()



if __name__ == "__main__":
    main()