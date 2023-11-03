import io
import socket
from picamera2 import Picamera2
import cv2
import time
from PIL import Image
from constant import *

class Client:
    def __init__(self):
        self.picam2 = Picamera2()
        self.picam2.preview_configuration.main.size = (480,640)
        self.picam2.preview_configuration.main.format = "RGB888"
        self.picam2.preview_configuration.align()
        self.picam2.configure("preview")
        self.picam2.start()
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.socket.settimeout(1)
        
        self.im=""    #사진 찍은 data
        self.image_bytes=None   #사진 찍은 data bytes단위
    def capture_image(self):
        self.im=self.picam2.capture_array()  #capture
        cv2.imwrite(CAPTUR_IMAGE_NAME,self.im)
    
    def open_image(self):
        
        with open(CAPTUR_IMAGE_NAME,'rb') as output_file:
            self.image_bytes=output_file.read()
        self.im=""
        
        
    def send_image(self):
        send_bytes=0
        left_bytes=len(self.image_bytes)
        #print(left_bytes)
        
        while send_bytes<len(self.image_bytes):
            now_send_bytes=min(MAX_SEND_BYTES,left_bytes)
            self.socket.sendto(self.image_bytes[send_bytes:MAX_SEND_BYTES+send_bytes],(UDP_IP,UDP_PORT))
            time.sleep(0.05)
            send_bytes+=now_send_bytes
            left_bytes-=now_send_bytes
            print(self.image_bytes[send_bytes:MAX_SEND_BYTES+send_bytes])
        self.socket.sendto(END_FLAG,(UDP_IP,UDP_PORT)) 
        
    def run_Camera(self):
        while True:
            chk=input("문을 닫아주십이오: (1 test)")
            if chk=="1":
                self.capture_image()
                self.open_image()
                self.send_image()
            else:
                break
                
                
if __name__=="__main__":
    cli=Client()
    cli.run_Camera()