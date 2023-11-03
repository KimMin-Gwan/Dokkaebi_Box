from ChatBot import *
from DBMS import *
from ChatBot.ChatBotData import *
from constant import *
from datetime import datetime
import mpu
import socket
import io
from PIL import Image
import random
from typing import Any
from flask import Flask, request
import numpy as np
class Web_Controller:
    def __init__(self, model,info):
        self.model = model 
        self.chat_bot_find= None   #chat 봇 클래스  find 챗봇 클래스이다. 
        self.info=info
        self.chat_bot_hand_over=None   #chat 봇 클래스 hand_over 챗봇 클래스이다.
        self.find_data_find=Dokkaebi_Data()  #chat bot을 통해 찾은 data class
        self.hand_over_data=Dokkaebi_Data()   #chat bot을 통해 hand_over 할 data class이다.

    def mainpage(self):
        return {"message":"Welcom To Dokkaebi Box"}
    
    def hand_over(self):
        self.chat_bot_hand_over=dokkaebi_ChatBot_Handover(self.hand_over_data)  #self.hand_over_data를 챗봇을 통해서 찾는다
        self.hand_over_data=self.chat_bot_hand_over.runChatBot()  #챗봇을 통해서 맡길 데이터를입력 받는다. 
        manager = Hand_Over(self.hand_over_data,self.info) #hand_over class실행
        manager.run_hand_over()  #handover 함수 실행  

    def find(self): 
        #self.chat_bot_find=dokkaebi_ChatBot_Find(self.find_data_find)
        #self.find_data_find=self.chat_bot_find.runChatBot()
        find_manager=Find(self.chat_bot.dokkaebi_data)
        final_data=find_manager.find_data_base() #최종 데이터 추후 작업은 이어서 예정
        #시나리오 작성 예시 ...... g

        return final_data  #이미지가 저장되어있는 경로를 return한다.
    
    def get_bot(self):
        self.chat_bot = dokkaebi_ChatBot_Handover(self.hand_over_data)
        self.manager = Hand_Over(self.hand_over_data, self.info)
        return self.chat_bot
    
    def get_image_data(self):
        image_path =SAVE_IMAGE_PATH+str(self.info.get_img_num())+".jpg"
        return image_path

    def get_item_data(self):
        return_dict = {}
        result = self.hand_over_data
        return_dict['losttime'] = result.lostTime
        return_dict['date'] = result.Date
        return_dict['lng'] = result.lng
        return_dict['let'] = result.lat
        return_dict['lostplace'] = result.lostplace
        return_dict['classification'] = result.classification
        #result = result.pop('path')
        return return_dict

    
    def save_data_now(self):
        #self.find_data_find = self.chat_bot_find.dokkaebi_data
        self.hand_over_data = self.chat_bot_hand_over.dokkaebi_data
        self.manager = Hand_Over(self.hand_over_data, self.info)
        self.manager.run_hand_over()
        return 
        
    


class Hand_Over():

    def __init__(self,data,info):
        self.info=info
        self.hand_over_data=data  #맡길 데이터 데이터베이스에 올라갈것이다.
        self.dbms=DataBase() 
        self.qury_data={} 

    def input_data_base(self):
        self.qury_data[CLASSIFICATION]=self.hand_over_data.classification  #종류
        self.qury_data[LOSTPLACE]=self.hand_over_data.lostplace  #잃어버린 위치
        self.qury_data[PATH]= SAVE_IMAGE_PATH+str(self.info.get_img_num())+".jpg"  #이미지 save_path
        self.qury_data[LOSTTIME]=self.hand_over_data.lostTime  #잃어버린 시간
        self.qury_data[LAT]=self.hand_over_data.lat  #위도  
        self.qury_data[LNG]=self.hand_over_data.lng  #경도
        self.qury_data[PWD]=self.hashcode()  #비밀번호 
        self.qury_data[STATE] = "보관"
        self.dbms.input_data(self.qury_data)

    def receive_data(self):   #여기서 udp통신을 통해서 라즈베리파이로 부터 사진 이미지를 받아온다.
        self.udp_controller.recevie_data()  # 캡처 이미지 하는 함수 
        self.udp_controller.save_picture()  


    def run_hand_over(self):
        self.udp_controller=UDP(self.info)
        self.receive_data()  #먼저 사진을 받아오고
        #그다음 사진이 유호한지는 추후 민관 개발
        self.input_data_base()   #database에 저장한다.

    def hashcode(self):
        code=str(random.randrange(1,100000))
        return code


class Find():  #Find 관련 함수 구현 예정
    def __init__(self,data) -> None:
        self.data=data   #데이터 베이스에서 찾을 데이터 Dokkaebi_Data class 형태로 구현 바로 직접 접근
        self.dbms= DataBase()  #database class호출후 사용
        self.find_result=None
    

    """
    1순위 : 날짜
    2순위 : 카테고리
    3순위 : 시간
    4순위 : 위치기반
    일단 날짜랑 카테고리는 default라 생각하고 시간만 계산 한다. 위치는 추후 계산 
    """
    
    def find_data_base(self):
        
        #1 2 순위는 항상 입력되었다 생각하고 
        if self.data.classification !=None :  #분류 날짜
            qury_data={CLASSIFICATION:self.data.classification}
            all_data=self.dbms.find_data(qury_data)   #data베이스에서 1 2 순위 싹다 뽑아오고
        #그다음 시간에 대해서 가장 작은 시간 범위를 찾는다.
        dt_temp,day_list_temp=self.find_date(self.data.Date,all_data)
    

        self.find_result=self.find_dist(self.data,day_list_temp,dt_temp)  #self.data는 찾아야할 데이터 day_list는 그냥 날짜 dt_temp는 결과 느낌?

    
        return self.find_result  #최종적으로 잃어버린 날짜 + 카테고리 + 시간에 대해서 찾은뒤 return해준다. 

    def find_date(self,target_date,data_list):
        month_list=[0,31,28,31,30,31,30,31,31,30,31,30,31]
        now_month=datetime.today().month
        now_day=datetime.today().day
        result_date=[[],[],[],[],[],[]]
        day_list=[]
        day_start=1
        day_list.append(target_date)
        for i in range(1,6):  #총 6일을 갈껀데 만약에 달이넘어가면 그다음달로 검색해야하잖아
            if(int(target_date[2:4])+i) >month_list[int(target_date[0:2])]:  #즉 일수가 현재 자기 달의 마지막 일보다 많아지면
                day_list.append(str(int(target_date[0:2])+1)+"0"+str(day_start))
                day_start+=1
            else:
                if(len(str(int(target_date[2:4])+i))==1):
                    day_list.append(target_date[0:2]+"0"+str(int(target_date[2:4])+i))
                else:
                    day_list.append(target_date[0:2]+str(int(target_date[2:4])+i))
        count_result_data=0 

        for day in day_list:
            for i in range(len(data_list)):
                if data_list[i][DATE]==day:
                    result_date[count_result_data].append(data_list[i])
            count_result_data+=1

        return result_date  ,day_list   #data_list 는 정렬된 데이터고 day_list는 추후 거리에 따라 정렬할때 
    

    def find_dist(self,target_place,day_list,data_list):
        for i in range(6):  #총 6일에 대한 데이터에 대해서 길이에 대해서 정렬할껀데
            if len(data_list[i]) !=0:
                for z in range(len(data_list[i])-1):
                    min_idx=z
                    for j in range(z+1,len(data_list[i])):
                        if mpu.haversine_distance((float(data_list[i][j]["let"]),float(data_list[i][j]["lng"])),(float(target_place.lat),float(target_place.lng)))<mpu.haversine_distance((float(data_list[i][min_idx]["let"]),float(data_list[i][min_idx]["lng"])),(float(target_place.lat),float(target_place.lng))):
                            min_idx=j
                    data_list[i][z],data_list[i][min_idx] =data_list[i][min_idx],data_list[i][z]
        
        return data_list






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
        
                
        
            
             
            
