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
from ChatBot import *
from konlpy.tag import Hannanum

class dokkaebi_ChatBot_Find:
    def __init__(self, data):
        self.hannanum = Hannanum()
        self.dokkaebi_data = data
        self.chatbot_data = pd.read_excel("C:\\Users\\antl\\Documents\\GitHub\\Dokkaebi_Box\\Develop\\jaehyun\\test\\ChatBot\\chatbot_data_find.xlsx")
        self.chat_dic = {}
        self.initChatBot()
        self.step = 1

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
                    nlp_result = self.hannanum.nouns(request)
                    month = nlp_result[0][:nlp_result[0].rfind('월')]
                    day = nlp_result[1][:nlp_result[1].rfind('일')]
                    hour = nlp_result[2][:nlp_result[2].rfind('시')]
                    minute = hour = nlp_result[3][:nlp_result[3].rfind('분')]
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
                return dokkaebi_response_str
        return '무슨 말인지 모르겠어요'

    def runChatBot(self):
        print("Seoul, my soul. 안녕하세요? 한강 도깨비 박스입니다.")
        while True:
            if self.step == 1:
                print("어떤 물건을 찾으러 오셨나요?(스마트폰/지갑/기타)")
                while True:
                    userResponse = input('입력 : ')
                    chatBotResponse = self.chat(userResponse)
                    print('도깨비박스 :', chatBotResponse)
                    if self.step != 1:
                        break
            elif self.step == 2:
                print("물건을 언제 분실하셨나요? ex) 11월 3일 13시 30분")
                while True:
                    userResponse = input('입력 : ')
                    chatBotResponse = self.chat(userResponse)
                    print('도깨비박스 :', chatBotResponse)
                    if self.step != 2:
                        break
            #elif self.step == 3:
            #    print("물건을 어디에서 잃어버리셨나요?")
            #    while True:
            #        userResponse = input('입력 : ')
            #        chatBotResponse = self.chat(userResponse)
            #        print('도깨비박스 : ', chatBotResponse)
            elif self.step == 3:
                print("도깨비 박스가 열렸습니다. 물건을 찾은 뒤 박스를 닫아주세요.")
                print("마음이 모이면 서울이 됩니다. Seoul, my soul")
                return self.dokkaebi_data


if __name__ == "__main__":
    DokkaebiChatBot_Data = Dokkaebi_Data()
    chatBot = dokkaebi_ChatBot_Find(DokkaebiChatBot_Data)
    chatBot.runChatBot()