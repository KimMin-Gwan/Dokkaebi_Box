import time

from dokkaebi_Cam import *
from dokkaebi_QRReader import *
from dokkaebi_MagneticSensor import *
from dokkaebi_MagneticSensor.MagneticSensor import dokkaebi_Magneticsensor
from dokkaebi_Servo import *
import threading
class dokkaebi_Raspberry:
    def __init__(self):
        self.dokkaebi_Rasp_Cam = clsdokkaebi_Box_Cam()
        self.dokkaebi_Rasp_Servo = dokkaebi_Servo()
        self.dokkaebi_Rasp_QRReader = dokkaebi_BarcodeReader(self.dokkaebi_Rasp_Servo)
        self.dokkaebi_Rasp_Magnetic = dokkaebi_Magneticsensor(self.dokkaebi_Rasp_Cam, self.dokkaebi_Rasp_Servo)

    def run_dokkaebi_Raspberry(self):
        qrread_thread=threading.Thread(target=self.dokkaebi_Rasp_QRReader.runQRReader)
        mag_thread=threading.Thread(target=self.dokkaebi_Rasp_Magnetic.runMagneticSensor)
        qrread_thread.start()
        mag_thread.start()
 


