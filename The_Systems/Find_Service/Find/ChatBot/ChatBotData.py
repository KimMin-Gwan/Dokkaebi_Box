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

class Dokkaebi_Data:
    def __init__(self):
        self.lostItem = None    # 사용자가 입력한 이름(스마트폰, 지갑, 화장품 등)
        self.classification = None # 분류(cellphone, wallet, etc)
        self.Date = None        # 11월 3일이면 1103
        self.lostTime = None    # 15시 30분이면 1530
        self.lostplace = None   # 사용자가 입력한 분실/습득장소(반포한강공원)
        self.lat = None # latitude 위도
        self.lng =None  # longitude 경도
        """ 서울시 위도 경도 경계
                  37.715133
        126.734086  서울시  127.269311      
                  37.413294
        """
