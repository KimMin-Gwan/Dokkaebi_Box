"""
* Project : 2023 Seoul AIOT Hackathon
* Program Purpose and Features :
* - class information
* Author : JH KIM
* First Write Date : 2023.11.03
* ==========================================================================
* Program history
* ==========================================================================
* Author    		Date		    Version		History
* JH KIM            2023.11.03		v1.00		First Write
"""

class clsInformation:
    def __init__(self):
        self.QRcodeData = ""    # QRcode data
        self.servoDeg = 0
        self.find_data={}   #찾을 데이터입력
        self.input_data={}   #맡길 데이터 입력
    def setQRcodeData(self, data):
        self.QRcodeData = data

    def getQRcodeData(self):
        return self.QRcodeData

    def setFindData(self,data):   #찾을 물품 관련 데이터  
        for i in data.keys():
            self.find_data[i]=data[i]

    def getFindData(self):
        return self.find_data
        
    def setInputData(self,data):   #맡길 데이터 
        for i in data.keys():   #dict 로 구현해 추후 경로랑 비밀번호 업데이트시 사용할수있다.
            self.input_data[i]=data[i]
    def getInputData(self):
        return self.input_data
    
 