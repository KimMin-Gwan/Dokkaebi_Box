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
    info = clsInformation()     # information class instance
    bcdReader = clsBarcodeReader(info)  # barcodeReader class instance
    svMotor = clsServoMotor(12)         # servoMortor class instance

    # barcode thread
    bcdReader_thread = Thread(target=bcdReader.runQRReader)
    bcdReader_thread.start()
   
   
    
    while True:
        # time.sleep(0
        # if info.getQRcodeData() == "antl":  # barcode 내용이 antl이면 잠금
        #     svMotor.setDegree(90,1)
        # elif info.getQRcodeData() == "YU":  # barcode 내용이 YU이면 열림
        #     svMotor.setDegree(0,1)

        time.sleep(0.1)
        if bcdReader.Chk_QrCode()==1:
            svMotor.setDegree(90,1)
        



if __name__ == "__main__":
    main()