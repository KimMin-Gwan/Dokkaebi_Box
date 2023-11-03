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
* JH KIM            2023.11.03      v1.10       Update geopy
"""

import pandas as pd
from ChatBotData import *
from konlpy.tag import Okt, Hannanum
from geopy.geocoders import Nominatim
from Constant import *
import re

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
        self.lang = "Ko"  # default = Ko

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
                    if self.lang == "Ko":
                        nlp_result = self.Okt.morphs(request)
                        if len(nlp_result) != 4:
                            break
                    elif self.lang == "En":
                        enResponse = re.split('[/: ]', request)
                        if len(enResponse) != 4:
                            break
                    if self.lang == "Ko":
                        month = nlp_result[0][:nlp_result[0].rfind('월')]
                        day = nlp_result[1][:nlp_result[1].rfind('일')]
                        hour = nlp_result[2][:nlp_result[2].rfind('시')]
                        minute = nlp_result[3][:nlp_result[3].rfind('분')]
                        dokkaebi_response_str = month + "월 " + day + "일 " + hour + "시 " + minute + "분에 분실하셨군요"
                    elif self.lang == "En":
                        month = enResponse[1]
                        day = enResponse[0]
                        hour = enResponse[2]
                        minute = enResponse[3]
                        dokkaebi_response_str = "You lost it at " + day + "/" + month + " " + hour + ":" + minute +", Right?"
                    if len(month) == 1:
                        month = "0" + month
                    if len(day) == 1:
                        day = "0" + day
                    if len(hour) == 1:
                        hour = "0" + hour
                    if len(minute) == 1:
                        minute = "0" + minute
                    self.dokkaebi_data.Date = month + day
                    self.dokkaebi_data.lostTime = hour + minute
                    self.step += 1
                self.rspFlag = 0
                return dokkaebi_response_str
        return '무슨 말인지 모르겠어요' if self.lang == "Ko" else "Sorry, I can't understand"

    def geocoding(self, address):
        geolocoder = Nominatim(user_agent='South Korea', timeout=None)
        geo = geolocoder.geocode(address)
        crd = {"lat": str(geo.latitude), "lng": str(geo.longitude)}
        return crd

    def getClassificationFromUserChat(self, usrResponse):   # 기존 step 1
        # print("어떤 물건을 찾으러 오셨나요?(스마트폰/지갑/기타)(What do you want to find?)(smartphone/wallet/etc)")
        userResponse = usrResponse.replace('이요', "")
        userResponse = self.Okt.morphs(userResponse)
        if len(userResponse) > 0:
            if userResponse[0].encode().isalpha():
                self.lang = "En"
        for rsp in userResponse:
            chatBotResponse = self.chat(rsp)
            if self.rspFlag == 0:
                self.dokkaebi_data.lostItem = rsp
                chatBotResponse += "물건을 언제 습득하셨나요? ex) 11월 3일 13시 30분" if self.lang == "Ko" else "When did you acquire the item? ex) dd/mm 15:30"
                break
        return chatBotResponse, self.rspFlag      # 첫번쨰 응답(스마트폰을 주우셨군요),(0(정상) or 1(알수 없는 응답))

    def getDateTimeFromUserChat(self, usrResponse): # 기존 step 2
        self.rspFlag = 1
        # print("물건을 언제 분실하셨나요? ex) 11월 3일 13시 30분"if self.lang == "Ko"else "When did you lost the item? ex) dd/mm 15:30")
        #userResponse = input('입력(Input) : ')
        userResponse = usrResponse[:usrResponse.rfind('분') + 1]
        # if self.lang == "En":
        #    EnResponse = re.split('[/: ]', userResponse)
        chatBotResponse = self.chat(userResponse)
        if self.rspFlag == 0:
            chatBotResponse += "물건을 어디에서 잃어버리셨나요?"if self.lang == "Ko" else "Where did you lost it?"
        return chatBotResponse, self.rspFlag

    def getPlaceFromUserChat(self, usrResponse):    # 기존 step 3
        self.rspFlag = 1
        dokkaebi_Response = '무슨말인지 잘 모르겠어요' if self.lang == "Ko" else "Sorry, I can't understand"

        userResponse = usrResponse.replace('이요', "")
        if self.lang == "Ko":
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
                        #print('{}을(를) 습득하신 곳은 {} 이군요.'.format(self.dokkaebi_data.lostItem, self.dokkaebi_data.lostplace))
                        dokkaebi_Response = '{}을(를) 분실하신 곳은 {} 이군요.'.format(self.dokkaebi_data.lostItem, self.dokkaebi_data.lostplace)
                        self.rspFlag = 0
                        return dokkaebi_Response, self.rspFlag
                    dokkaebi_Response = '입력하신 곳은 도깨비박스 서비스 지역이 아닙니다.' if self.lang == "Ko" else "The location you entered is not a service area."
                except:
                    continue
        else:
            try:
                crd = self.geocoding(userResponse)
                if float(crd['lat']) >= SEOULLOWERBOUNDARY and float(
                        crd['lat']) <= SEOULUPPERBOUNDARY and float(
                    crd['lng']) <= SEOULRIGHTBOUNDARY and float(crd['lng']) >= SEOULLEFTBOUNDARY:
                    self.geopyFlag = 0
                    self.dokkaebi_data.lostplace = userResponse
                    self.dokkaebi_data.lat = crd['lat']
                    self.dokkaebi_data.lng = crd['lng']
                    #print('You find the {} at {}. Right?'.format(self.dokkaebi_data.lostItem,self.dokkaebi_data.lostplace))
                    dokkaebi_Response = 'You find the {} at {}. Right?'.format(self.dokkaebi_data.lostItem,self.dokkaebi_data.lostplace)
                    self.rspFlag = 0
                    return dokkaebi_Response, self.rspFlag
            except:
                dokkaebi_Response = "The location you entered is not a service area."
        # crd = geocoding("서울역")
        # crd = geocoding("동대구역")
        # crd = geocoding("영남대")
        return dokkaebi_Response, self.rspFlag

    def endingMent(self):
        if self.lang == "Ko":
            #print("감사합니다. 도깨비박스가 물건을 잘 보관할게요.")
            #print("마음이 모이면 서울이 됩니다. Seoul, my soul")
            return "도깨비박스가 열렸습니다. 물건을 찾은 뒤 박스를 닫아주세요.\n마음이 모이면 서울이 됩니다. Seoul, my soul"
        else:
            #print("Dokkaebi Box will keep the goods safe. Thank you")
            #print("Seoul, my soul")
            return "Dokkaebi Box is opened. Please close the door after taking out the item\nSeoul, my soul"

    def runChatBot(self):
        print("Seoul, my soul. 안녕하세요? 한강 도깨비 박스입니다.(Hello, I am the Dokkaebi Box)")
        while True:
            if self.step == 1:
                while True:
                    print("어떤 물건을 찾으러 오셨나요?(스마트폰/지갑/기타)(What do you want to find?)(smartphone/wallet/etc)")
                    userResponse = input('입력(Input) : ').replace('이요', "")
                    userResponse = self.Okt.morphs(userResponse)
                    if len(userResponse) > 0:
                        if userResponse[0].encode().isalpha():
                            self.lang = "En"
                    for rsp in userResponse:
                        chatBotResponse = self.chat(rsp)
                        if self.rspFlag == 0:
                            self.dokkaebi_data.lostItem = rsp
                            break
                    print(chatBotResponse)
                    if self.step != 1:
                        break
            elif self.step == 2:
                while True:
                    print("물건을 언제 분실하셨나요? ex) 11월 3일 13시 30분"if self.lang == "Ko"else "When did you lost the item? ex) dd/mm 15:30")
                    userResponse = input('입력(Input) : ').replace('이요', "")
                    chatBotResponse = self.chat(userResponse)
                    print(chatBotResponse)
                    if self.step != 2:
                        break
            elif self.step == 3:
                print("물건을 어디에서 잃어버리셨나요?"if self.lang == "Ko" else "Where did you lost it?")
                while True:
                    dokkaebi_Response = '무슨말인지 잘 모르겠어요'if self.lang == "Ko" else "Sorry, I can't understand"
                    userResponse = input('입력(Input) : ').replace('이요',"")
                    if self.lang == "Ko":
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
                                dokkaebi_Response = '입력하신 곳은 도깨비박스 서비스 지역이 아닙니다.' if self.lang == "Ko" else "The location you entered is not a service area."
                            except:
                                continue
                    else:
                        try:
                            crd = self.geocoding(userResponse)
                            if float(crd['lat']) >= SEOULLOWERBOUNDARY and float(
                                    crd['lat']) <= SEOULUPPERBOUNDARY and float(
                                crd['lng']) <= SEOULRIGHTBOUNDARY and float(crd['lng']) >= SEOULLEFTBOUNDARY:
                                self.geopyFlag = 0
                                self.dokkaebi_data.lostplace = userResponse
                                self.dokkaebi_data.lat = crd['lat']
                                self.dokkaebi_data.lng = crd['lng']
                                print('You find the {} at {}. Right?'.format(self.dokkaebi_data.lostItem,
                                                                             self.dokkaebi_data.lostplace))
                        except:
                            dokkaebi_Response = "The location you entered is not a service area."
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
                if self.lang == "Ko":
                    print("도깨비박스가 열렸습니다. 물건을 찾은 뒤 박스를 닫아주세요.")
                    print("마음이 모이면 서울이 됩니다. Seoul, my soul")
                else:
                    print("Dokkaebi Box is opened. Please close the door after taking out the item")
                    print("Seoul, my soul")
                return self.dokkaebi_data


if __name__ == "__main__":
    DokkaebiChatBot_Data = Dokkaebi_Data()
    chatBot = dokkaebi_ChatBot_Find(DokkaebiChatBot_Data)
    chatBot.runChatBot()