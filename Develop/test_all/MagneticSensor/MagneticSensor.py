"""
* Project : 2023 Seoul AIOT Hackathon
* Program Purpose and Features :
* - class dokkaebi_MagneticSensor
* Author : JH KIM
* First Write Date : 2023.11.03
* ==========================================================================
* Program history
* ==========================================================================
* Author    		Date		    Version		History
* JH KIM            2023.11.03		v1.00		First Write
* JH KIM            2023.11.03		v1.10		Sensor Detect method Polling -> Interupt
"""

import RPi.GPIO as GPIO #import the GPIO library
import time
from magneticConstant import *

class clsMagneticSensor:
    def __init__(self):
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(MAGNETIC_DEFAULT_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        self.magneticDoorState = False # False(닫힘)/True(열림)

    def setMagnetic_open(self):
        self.magneticDoorState = True

    def setMagnetic_close(self):
        self.magneticDoorState = False

    def getMagneticDoorState(self):
        return

    def runMagneticSensor(self):
        Ser
        while True:
            print(1)
            if GPIO.wait_for_edge(MAGNETIC_DEFAULT_PIN, GPIO.FALLING, bouncetime=200) == MAGNETIC_DEFAULT_PIN:
                self.setMagnetic_close()
                print("SYSTEM MESSAGE::The door closed")
            if GPIO.wait_for_edge(MAGNETIC_DEFAULT_PIN, GPIO.RISING, bouncetime=200) == MAGNETIC_DEFAULT_PIN:
                self.setMagnetic_open()
                print("SYSTEM MESSAGE::The door opened")
        """
                while True:
            if GPIO.input(MAGNETIC_DEFAULT_PIN) == GPIO.HIGH:
                print("SYSTEM MESSAGE::The door closed")
            elif GPIO.input(MAGNETIC_DEFAULT_PIN) == GPIO.LOW:
                print("SYSTEM MESSAGE::The door opened")
        """


if __name__ == "__main__":
    mag = clsMagneticSensor()
    mag.runMagneticSensor()