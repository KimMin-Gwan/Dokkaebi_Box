"""
* Project : 2023 Seoul AIOT Hackathon
* Program Purpose and Features :
* - dokkaebi box priority algorithms
* Author : JH KIM
* First Write Date : 2023.11.03
* ==========================================================================
* Program history
* ==========================================================================
* Author    		Date		    Version		History
* JH KIM            2023.11.03		v1.00		First Write
* JH KIM            2023.11.03      v1.10       Update geopy
"""

import mpu

lat1 = 37.715133
lon1 = 126.734086

lat2 = 37.413294
lon2 = 127.269311

start = (37.715133, 126.734086)
goal = (37.413294, 127.269311)

lostT = "1130"
findT = "1500"

class dokkaebiBox_Priority:
    def __init__(self):
        self.start = None       # (lat,lng) tuple
        self.goal = None        # (lat,lng) tuple
        self.diff_distance = None   # float km
        self.lostTime = None    # str
        self.findTime = None    # str
        self.diff_time = None
        self.priority = None

    def calPriority(self):
        self.diff_distance = mpu.haversine_distance(start, goal)
        print("diff_distance", self.diff_distance)
        self.diff_time = int(self.findTime[0:2])*60 + int(self.findTime[2:]) - (int(self.lostTime[0:2])*60 + int(self.lostTime[2:]))
        print("diff_Time", self.diff_time)
        self.priority = self.diff_distance + float(self.diff_time)
        print(self.priority)

def main():
    dok = dokkaebiBox_Priority()
    dok.start = start
    dok.goal = goal
    dok.findTime = findT
    dok.lostTime = lostT
    dok.calPriority()

if __name__ == "__main__":
    main()

