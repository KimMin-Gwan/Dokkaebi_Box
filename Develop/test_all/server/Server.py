import socket
import numpy
import cv2
import io
from PIL import Image
from server.constant import *
import random
from typing import Any
from flask import Flask, request
import numpy as np
from pymongo import MongoClient# pymongo 임포트
from PIL import Image
from server.constant import *

from DataBase import *

class Server:
    def __init__(self,info):
        self.socket=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
        self.socket.bind((UDP_IP,UDP_PORT))
        self.picture=b''
        self.info=info
        self.path=SAVE_IMAGE_PATH
        self.img_num=0
        self.save_path=f"{SAVE_IMAGE_PATH}{self.img_num}.jpg"
        self.QRPASSORD=""
        self.qury_data={}
        self.db=Database(info) 
    def save_picture(self):
        image_stram=io.BytesIO(self.picture)
        image=Image.open(image_stram)
        #image.show()
        #print(save_path)
        image.save(self.save_path)
        self.img_num+=1

    def get_imge_path(self):
        self.qury_data["path"]=self.save_path
    
    def hashcode(self):
        self.QRPASSORD=random.randrange(1,200000)
        self.qury_data["PWD"]=self.QRPASSORD
        
    def recevie_data(self):
        self.picture=b''
        while True:
            data,addr=self.socket.recvfrom(MAX_SEND_BYTES)
            if data == END_FLAG:
                break 
            self.picture+=data
    def makeInputDataDict(self):
        data={}
        data["path"]=self.get_imge_path()
        data["PWD"]=self.hashcode()
        return data

    
    def question_data(self):  #추후 챗봇을 통해 이쪽으로 데이터가 들어올예정이므로 삭제 할 함수
        date=int(input("날짜는 언제인가요?"))
        category=input("카테고리는 무엇인가요?") 
        location=input("잃어버린 위치는 어디인가요?")
        time=("찾은 시간은 언제인가요?")
        self.qury_data['date']=date
        self.qury_data['category']=category
        self.qury_data['location']=location
        self.qury_data['time']=time
       
    def run_server(self):
        while True:
            num=input("1번 find 2번 input") 
            if num=="1":
                self.question_data()
            elif num=="2":
                self.question_data()  #습득 물품의 기본 정보를 입력받고
                self.recevie_data()  #사진 정보를 전달받고
                self.get_imge_path()
                self.hashcode()
                self.db.input_data(self.qury_data)
                self.qury_data={}

if __name__=="__main__":
    ser=Server()
    ser.recevie_data()    