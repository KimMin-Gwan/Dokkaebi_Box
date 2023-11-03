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
        self.info=info
        self.picture=b''
        self.path=SAVE_IMAGE_PATH
        self.save_path=f"{SAVE_IMAGE_PATH}"
        self.QRPASSORD=""
        self.qury_data={}


    def save_picture(self):  #사진 저장 함수
        image_stram=io.BytesIO(self.picture)
        image=Image.open(image_stram)
        image.save(self.save_path+str(self.info.get_img_num())+".jpg")
        self.info.set_img_num()
        
    def get_imge_path(self):
        self.qury_data["path"]=self.save_path  #이미지 경로 저장
    
        
    def recevie_data(self):
        self.picture=b''
        while True:
            data,addr=self.socket.recvfrom(MAX_SEND_BYTES)
            if data == END_FLAG:
                break 
            self.picture+=data
            
    def capture_image(self):
        self.recevie_data()
        self.save_picture()
        