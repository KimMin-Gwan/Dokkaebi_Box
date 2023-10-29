"""
* Project : 2023 Seoul AIOT Hackathon
* Program Purpose and Features :
* - test Main
* Author : JH KIM
* First Write Date : 2023.11.03
* ==========================================================================
* Program history
* ==========================================================================
* Author    		Date		    Version		History
* JH KIM            2023.11.03		v1.00		First Write
"""
import time

from Information import *
from QRReader import *
from ServoMotor import *
from threading import Thread
def main():
    info = clsInformation()
    bcdReader = clsBarcodeReader(info)
    svMotor = clsServoMotor(12)

    bcdReader_thread = Thread(target=bcdReader.runQRReader)
    bcdReader_thread.start()
    while True:
        time.sleep(0.1)
        if info.getQRcodeData() == "antl":
            svMotor.setDegree(90,1)
        elif info.getQRcodeData() == "YU":
            svMotor.setDegree(0,1)



if __name__ == "__main__":
    main()