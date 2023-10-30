from constant  import *
import random
class clsbox:
    def __init__(self) -> None:
        self.boxlist=["A1","A2","A3"]  #박스 하나만 구현하기때문에
    
    def find_item(self,box_loc):
        self.boxlist.append(box_loc)

    def put_item(self):
        if len(self.boxlist)==MAX_BOX_SPACE:
            print("상자가 다 찼습니다. 이용 불가능 합니다.")
        else:
            box_location=random.randrange(0,len(self.boxlist))
            return self.boxlist[box_location]