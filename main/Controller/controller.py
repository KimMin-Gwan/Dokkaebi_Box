from ChatBot import *
from Model.DBMS import *
from ChatBot.ChatBotData import *
from constant import URL
import requests

class Web_Controller():
    def __init__(self, model):
        self.model = model
        self.chat_bot_hand_over= None   #chat 봇 클래스  
        self.chat_bot_find= None   #chat 봇 클래스  
        self.hand_over_data_find=Dokkaebi_Data()  #chat bot을 통해 찾은 data class
        self.find_data_find=Dokkaebi_Data()  #chat bot을 통해 찾은 data class
    def mainpage(self):
        return {"message":"Welcom To Dokkaebi Box"}
    
    def hand_over(self, device_id, client_id=0, temp_id=0):
        
        device_manager = self.model.get_device_manager()
        if not device_manager.search_device(device_id):
            return {"message":"Bad Device_id"}       

        manager = Hand_Over(self.hand_over_data_find) # 문이 열림

        self.chat_bot_hand_over = dokkaebi_ChatBot_Handover(self.hand_over_data_find)
        self.hand_over_data_find=self.chat_bot_hand_over.runChatBot()

        manager.take_picture(self)




    def find(self):
        
        self.chat_bot_find=dokkaebi_ChatBot_Find(self.find_data_find)
        self.find_data_find=self.chat_bot_find.runChatBot()
        
        find_manager=Find(self.find_data_find)
        final_data=find_manager.find_data_base() #최종 데이터 추후 작업은 이어서 예정
        
        #시나리오 작성 예시 ......       
        return final_data["path"]  #이미지가 저장되어있는 경로를 return한다.
    

class Hand_Over():
    def __init__(self, device_id):
        self.device_id = device_id
        req_str = URL+str(device_id)+"/open"
        response = requests.get(req_str)

    def take_picture(self):
        # 디바이스에 사진촬영을 요구하는 requset를 보냄
        pass

    def save_data
            




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
        if self.data.classification !=None and self.data.Date!=None:
            qury_data={"category":self.data.classification,"date":self.data.Date}
            all_data=self.dbms.find_data(qury_data)
        
        #그다음 시간에 대해서 가장 작은 시간 범위를 찾는다.
        
        if len(all_data) !=0: 
            print(self.data.lostTime)
            tartget_time=self.data.lostTime
            self.find_result=self.find_closet_time(tartget_time,all_data)
        
        return self.find_result  #최종적으로 잃어버린 날짜 + 카테고리 + 시간에 대해서 찾은뒤 return해준다. 

    
    
    def find_closet_time(a,target_data,list_data):
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
                    
                
        
            
             
            
