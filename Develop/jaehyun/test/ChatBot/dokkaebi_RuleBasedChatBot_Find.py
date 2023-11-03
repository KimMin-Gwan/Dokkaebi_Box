"""
* Project : 2023 Seoul AIOT Hackathon
* Program Purpose and Features :
* - class dokkaebi_RuleBasedChatBot_Find
* Author : JH KIM
* First Write Date : 2023.11.03
* ==========================================================================
* Program history
* ==========================================================================
* Author    		Date		    Version		History
* JH KIM            2023.11.03		v1.00		First Write
"""
import pandas as pd
from ChatBotData import *
from konlpy.tag import Okt, Hannanum
from geopy.geocoders import Nominatim
from Constant import *
class dokkaebi_ChatBot_Find:
    def __init__(self, data):
        self.Okt = Okt()
        self.Hannanum = Hannanum()
        self.dokkaebi_data = data
        self.chatbot_data = pd.read_excel("chatbot_data_find.xlsx")
        self.chat_dic = {}
        self.initChatBot()
        self.step = 1
        self.geopyFlag = 1   # 0 (정상 입력)/ 1(잘못된 입력)
        self.rspFlag = 1 # 챗봇이 정확하게 이해한 경우


    def initChatBot(self):
        # rule의 데이터를 split하여 list형태로 변환 후, index값과 함께 dictionary 형태로 저장
        row = 0
        for rule in self.chatbot_data['rule']:
            self.chat_dic[row] = rule.split('|')
            row += 1

    def chat(self, request):
        for k, v in self.chat_dic.items():
            index = -1
            for word in v:
                try:
                    if index == -1:
                        index = request.index(word)
                    else:
                        # 이전 index 값은 현재 index값보다 이전이어야 한다.
                        if index < request.index(word, index):
                            index = request.index(word, index)
                        else:  # index 값이 이상할 경우 과감하게 break를 한다
                            index = -1
                            break
                except ValueError:
                    index = -1
                    break
            if index > -1:
                if self.chatbot_data['type'][k] == "classification":
                    self.dokkaebi_data.classification = self.chatbot_data['data'][k]
                    dokkaebi_response_str = self.chatbot_data['response'][k]
                    self.step += 1
                elif self.chatbot_data['type'][k] == "time":
                    nlp_result = self.Okt.morphs(request)
                    if len(nlp_result) != 4:
                        break
                    month = nlp_result[0][:nlp_result[0].rfind('월')]
                    day = nlp_result[1][:nlp_result[1].rfind('일')]
                    hour = nlp_result[2][:nlp_result[2].rfind('시')]
                    minute = nlp_result[3][:nlp_result[3].rfind('분')]
                    dokkaebi_response_str = month+"월 " +day+"일 " +hour +"시 "+minute+"분에 분실하셨군요"
                    if len(month) == 1:
                        month = "0" + month
                    if len(day) == 1:
                        day = "0" + day
                    if len(hour) == 1:
                        hour = "0" + hour
                    if len(minute) == 1:
                        minute = "0" + minute
                    self.dokkaebi_data.Date = month+day
                    self.dokkaebi_data.lostTime = hour+minute
                    self.step+=1
                self.rspFlag = 0
                return dokkaebi_response_str
        return '무슨 말인지 이해하지 못했어요'
    def geocoding(self, address):
        geolocoder = Nominatim(user_agent='South Korea', timeout=None)
        geo = geolocoder.geocode(address)
        crd = {"lat": str(geo.latitude), "lng": str(geo.longitude)}

        return crd
    def runChatBot(self):
        print("Seoul, my soul. 안녕하세요? 한강 도깨비 박스입니다.")
        while True:
            if self.step == 1:
                while True:
                    print("어떤 물건을 찾으러 오셨나요?(스마트폰/지갑/기타)")
                    userResponse = input('입력 : ')
                    userResponse = self.Okt.morphs(userResponse)
                    for rsp in userResponse:
                        chatBotResponse = self.chat(rsp)
                        if self.rspFlag == 0:
                            self.dokkaebi_data.lostItem = rsp
                            print(rsp)
                            break
                    print(chatBotResponse)
                    if self.step != 1:
                        break
            elif self.step == 2:
                while True:
                    print("물건을 언제 분실하셨나요? ex) 11월 3일 13시 30분")
                    userResponse = input('입력 : ')
                    chatBotResponse = self.chat(userResponse)
                    print(chatBotResponse)
                    if self.step != 2:
                        break
            elif self.step == 3:
                print("물건을 어디에서 잃어버리셨나요?")
                while True:
                    dokkaebi_Response = '무슨말인지 잘 모르겠어요'
                    userResponse = input('입력 : ')
                    nlpResult = self.Hannanum.nouns(userResponse)
                    for rst in nlpResult:
                        try:
                            crd = self.geocoding(rst)
                            if float(crd['lat']) >= SEOULLOWERBOUNDARY and float(
                                    crd['lat']) <= SEOULUPPERBOUNDARY and float(
                                    crd['lng']) <= SEOULRIGHTBOUNDARY and float(crd['lng']) >= SEOULLEFTBOUNDARY:
                                self.geopyFlag = 0
                                self.dokkaebi_data.lostplace = rst
                                self.dokkaebi_data.lat = crd['lat']
                                self.dokkaebi_data.lng = crd['lng']
                                print('{}을(를) 분실하신 곳은 {} 이군요.'.format(self.dokkaebi_data.lostItem,
                                                                      self.dokkaebi_data.lostplace))
                                break
                            dokkaebi_Response = '입력하신 곳은 도깨비박스 서비스 지역이 아닙니다.'
                        except:
                            continue
                    if self.geopyFlag == 0:
                        self.step += 1
                        break
                    # crd = geocoding("서울역")
                    # crd = geocoding("동대구역")
                    # crd = geocoding("영남대")

                    print(dokkaebi_Response)
                    if self.step != 3:
                        break
            elif self.step == 4:
                print("도깨비 박스가 열렸습니다. 물건을 찾은 뒤 박스를 닫아주세요.")
                print("마음이 모이면 서울이 됩니다. Seoul, my soul")

                return self.dokkaebi_data


if __name__ == "__main__":
    DokkaebiChatBot_Data = Dokkaebi_Data()
    chatBot = dokkaebi_ChatBot_Find(DokkaebiChatBot_Data)
    chatBot.runChatBot()