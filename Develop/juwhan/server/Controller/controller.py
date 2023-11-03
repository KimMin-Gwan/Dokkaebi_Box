from ChatBot import *
from Model.DBMS import *
from ChatBot.ChatBotData import *
from Controller.constant import *
from Controller.UDP_Con import *
import math
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
        
        self.chat_bot_find=dokkaebi_ChatBot_Find(self.find_data_find)
        self.find_data_find=self.chat_bot_find.runChatBot()
        find_manager=Find(self.find_data_find)
        final_data=find_manager.find_data_base() #최종 데이터 추후 작업은 이어서 예정
        #시나리오 작성 예시 ...... 
        
        return final_data[PATH]  #이미지가 저장되어있는 경로를 return한다.
class Hand_Over():

    def __init__(self,data,info):
        self.info=info
        self.udp_controller=UDP(self.info)
        self.hand_over_data=data  #맡길 데이터 데이터베이스에 올라갈것이다.
        self.dbms=DataBase() 
        self.qury_data={} 

    def input_data_base(self):
        self.qury_data[CLASSIFICATION]=self.hand_over_data.classification
        self.qury_data[LOSTPLACE]=self.hand_over_data.lostplace
        self.qury_data[PATH]= SAVE_IMAGE_PATH
        self.qury_data[LOSTTIME]=self.hand_over_data.lostTime
        self.qury_data[LAT]=self.hand_over_data.lat
        self.qury_data[LNG]=self.hand_over_data.lng
        self.dbms.input_data(self.qury_data)

    def receive_data(self):   #여기서 udp통신을 통해서 라즈베리파이로 부터 사진 이미지를 받아온다.
        self.udp_controller.recevie_data()  # 캡처 이미지 하는 함수 
        self.udp_controller.save_picture()  


    def run_hand_over(self):
        self.receive_data()  #먼저 사진을 받아오고
        #그다음 사진이 유호한지는 추후 민관 개발
        self.input_data_base()   #database에 저장한다.



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
        if self.data.classification !=None and self.data.Date!=None:  #분류 날짜
            qury_data={CLASSIFICATION:self.data.classification,DATE:self.data.Date}

            all_data=self.dbms.find_data(qury_data)   #data베이스에서 1 2 순위 싹다 뽑아오고
        #그다음 시간에 대해서 가장 작은 시간 범위를 찾는다.
        if len(all_data) !=0: 
            print(self.data.lostTime)
            tartget_time=self.data.lostTime
            self.seconde_data=self.find_closet_time(tartget_time,all_data)

        if len(self.seconde_data):
            pass



        return self.find_result  #최종적으로 잃어버린 날짜 + 카테고리 + 시간에 대해서 찾은뒤 return해준다. 
    



    def find_closet_time(self,target_data,list_data):

        #target_data 는 사용자가입력한 시간데이터 1300 형식으로되어있을것
        #list_data에는 데이터 베이스에서 그대로 읽어온 데이터 리스트 형식
        #1315이면 13*60 + 15분으로 생각하고
        closet_min=25*60 
        target_min=int(target_data[0:2]) *60  +int(target_data[2:4])
        closet_min_data=None 
        for time in list_data:
            new_min=int(time["time"][0:2]) * 60 +int(time["time"][2:4])
            
            if(abs(target_min-new_min)<closet_min):
                closet_min=abs(target_min-new_min)
                closet_min_data=time
        return closet_min_data 
    
    def haversine(self,lat1, lon1, lat2, lon2):
    # 지구 반지름 (킬로미터)
        radius = 6371.0
        
        # 라디안으로 위도 경도 변환
        lat1 = math.radians(lat1)
        lon1 = math.radians(lon1)
        lat2 = math.radians(lat2)
        lon2 = math.radians(lon2)
        
        # Haversine 공식 계산
        dlon = lon2 - lon1
        dlat = lat2 - lat1
        a = math.sin(dlat/2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon/2)**2
        c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
        distance = radius * c
        
        return distance

    def find_closest_points(self,target_lat,target_lng,list_data):
        min_distance = float('inf')
        closest_points = None

        for i in range(len(list_data)):
            lat1, lon1 = target_lat,target_lng 
            lat2, lon2 = (list_data[i].lat,list_data[i].lng)
            distance = self.haversine(lat1, lon1, lat2, lon2)

            if distance < min_distance:
                min_distance = distance
                closest_points = list_data[i]

        return closest_points

        
                
        
            
             
            
