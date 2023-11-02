import socket
import numpy
import cv2
import io
from PIL import Image
import random
from typing import Any
from flask import Flask, request
import numpy as np
from Controller.constant import *



class UDP:

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


    def save_picture(self):  #사진 저장 함수
        image_stram=io.BytesIO(self.picture)
        image=Image.open(image_stram)
        image.save(self.save_path)
        self.img_num+=1  #사진이 저장될때마다 저장소 +=1 추후 category별로 나눌지는 상의
        
    def get_imge_path(self):
        self.qury_data["path"]=self.save_path  #이미지 경로 저장
    
    def hashcode(self):
        self.QRPASSORD=random.randrange(1,200000)
        self.QRPASSORD=str(self.QRPASSORD)
        self.qury_data["PWD"]=(self.QRPASSORD)
        
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
    def capture_image(self):
        self.recevie_data()
        self.save_picture()
        