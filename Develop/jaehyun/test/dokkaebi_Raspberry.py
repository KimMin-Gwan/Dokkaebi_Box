import time

from test.dokkaebi_Cam import *
from test.dokkaebi_QRReader import *
from test.dokkaebi_MagneticSensor import *
from test.dokkaebi_Servo import *

class dokkaebi_Raspberry:
    def __init__(self):
        self.dokkaebi_Rasp_Cam = dokkaebi_Box_Cam()
        self.dokkaebi_Rasp_Servo = dokkaebi_Servo()
        self.dokkaebi_Rasp_QRReader = dokkaebi_BarcodeReader(self.dokkaebi_Rasp_Servo)
        self.dokkaebi_Rasp_Magnetic = dokkaebi_MagneticSensor(self.dokkaebi_Rasp_Cam, self.dokkaebi_Rasp_Servo)

    def run_dokkaebi_Raspberry(self):
        dokkaebi_RaspberryPI = dokkaebi_Raspberry()
        dokkaebi_RaspberryPI.dokkaebi_Rasp_Magnetic.runMagneticSensor()


