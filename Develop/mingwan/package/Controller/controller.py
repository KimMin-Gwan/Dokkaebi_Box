from Model.DBMS import *


class Web_Controller():
    def __init__(self, model):
        self.model = model
        


    def mainpage(self):
        return {"message":"Welcom To Dokkaebi Box"}
    
    def hand_over(self, device_id):
        # 본인 인증
        manager = Hand_Over(device_id, self.model)
        




class Hand_Over():
    def __init__(self, data, model) -> None:
        self.data = data
    
    """
    1. 
    2. 
    3. 

    """




        

