import pandas as pd
from konlpy import *

class dokkaebi_ChatBot:
    def __init__(self):
        self.chatbot_data = pd.read_excel("chatbot_data.xlsx")
        self.chat_dic = {}
        self.initChatBot()

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
                return self.chatbot_data['response'][k]
        return '무슨 말인지 모르겠어요'

    def runChatBot(self):
        print("무엇을 도와드릴까요?")
        while True:
            req = input('입력:')
            if req == 'exit':
                break
            else:
                print('도깨비박스 : ', self.chat(req))


if __name__ == "__main__":
    chatBot = dokkaebi_ChatBot()
    chatBot.runChatBot()