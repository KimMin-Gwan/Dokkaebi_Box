#from ..View.main_view import main_test
from typing import Any
from flask import Flask, request
import numpy as np
from pymongo import MongoClient# pymongo 임포트
from PIL import Image
#from Model.constant import *

MONGODB_ADDR="mongodb+srv://sunjuwhan:ans693200@sunjuwhan.soaegl1.mongodb.net/"
CLIENT_LOC="IOT"   #상위
DB_LOC="image"  #하위 폴더

"""

{category :  "string"   , date:"20231031"     ,    time : "1101"    ,    loaction :  "추후 결정 "}


"""
class DataBase():
    def __init__(self):
        self.client=MongoClient(MONGODB_ADDR)
        self.db=self.client[CLIENT_LOC]
        self.collection=self.db[DB_LOC]
        self.return_data=[]
    def input_data(self,input_data):  
        self.collection.insert_one(input_data)

    def find_data(self,find_data):
        result=self.collection.find(find_data)
        for doc in result:
            self.return_data.append(doc) 
        return self.return_data  #find_data는 qury형태로 데이터를 find해서 return해준다. 