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
from DataBase import *

from server import *

from Information import *
#from dokkaebi_QRReader import *
#from dokkaebi_Servo import *
from threading import Thread
def main():
    info = clsInformation()     # information class instance
    #bcdReader = clsBarcodeReader(info)  # barcodeReader class instance
    #svMotor = clsServoMotor(12)         # servoMortor class instance

    # barcode thread
    #bcdReader_thread = Thread(target=bcdReader.runQRReader)
    #bcdReader_thread.start()
    
    
    server=Server(info)
    database=Database(info)

    server_thread=Thread(target=server.run_server)
    server_thread.start()
    

if __name__ == "__main__":
    main()