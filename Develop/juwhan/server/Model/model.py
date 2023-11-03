

class Model():
    def __init__(self, dbms):
        self.dbms = dbms
        self.device_manager = Device_Manager(self.dbms)
        self.client_id = Client_Id()

    def get_device_manager(self):
        return self.device_manager

class Device_Id:
    # 디바이스 아이디   여기는 말그대로 박스 위치에 대한 클래스 이고 
    def __init__(self, id =-1, loc = "", state = False, size = -1):
        self.id = id  # 아이디
        self.loc = loc # 위치
        self.state = state# 사용가능 여부
        self.size = size # 최대 
    
    def __call__(self):
        print(f"Pre-Selected Device")
        print(f"ID : {self.id} ")
        print(f"location : {self.loc} ")
        print(f"state : {self.state} ")
        print(f"size : {self.size} ")


class Client_Id:
    def __init__(self):
       pass 
class Device_Manager:
    def __init__(self, dbms):
        self.dbms = dbms
        self.device_list = []  # -> Device_ID
        self.get_device_data()

    def get_device_data(self):
        #result = self.dbms.get_device_data()  # DBMS 제작 요망

        #for data in result:
            #id = data['id']
            #loc = data['loc']
            #state = data['state']
            #size = data['size']
            #temp_device = Device_Id(id, loc, state, size)
            #self.device_list.append(temp_device)
            pass


        


