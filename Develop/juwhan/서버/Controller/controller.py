
class Web_Controller():
    def __init__(self, model):
        self.model = model
        


    def mainpage(self):
        return {"message":"Welcom To Dokkaebi Box"}
    
    def hand_over(device_id, client_id, temp_id):

        manager = Hand_Over()



class Hand_Over():
    def __init__(self):
        

