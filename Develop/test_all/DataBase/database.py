from typing import Any
from flask import Flask, request
import numpy as np
from pymongo import MongoClient# pymongo 임포트
from PIL import Image
from DataBase.constant import *

class Database:
    def __init__(self,info) -> None:
        self.client=MongoClient(MONGODB_ADDR)
        self.db=self.client[CLIENT_LOC]
        self.collection=self.db[DB_LOC]
        self.info=info

    def input_data(self,ip_dt):   #ip_dt는 넣을 데이터이다.ip_dt =   
        print(ip_dt)
        self.collection.insert_one(ip_dt)
    def find_data(self,fd_dt):
        pass
    