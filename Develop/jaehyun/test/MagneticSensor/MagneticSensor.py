"""
* Project : 2023 Seoul AIOT Hackathon
* Program Purpose and Features :
* - class MagneticSensor
* Author : JH KIM
* First Write Date : 2023.11.03
* ==========================================================================
* Program history
* ==========================================================================
* Author    		Date		    Version		History
* JH KIM            2023.11.03		v1.00		First Write
"""

import RPi.GPIO as GPIO #import the GPIO library
import time
from magneticConstant import *

class clsMagneticSensor:
    def __init__(self):
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(MAGNETIC_DEFAULT_PIN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        self.magneticState = False # False(닫힘)/True(열림)
        GPIO.add_event_detect(MAGNETIC_DEFAULT_PIN, GPIO.FALLING, callback=self.setMagnetic_close, bouncetime=200)
        #GPIO.add_event_detect(MAGNETIC_DEFAULT_PIN, GPIO.RISING, callback=self.setMagnetic_open, bouncetime=200)

    #def runMagneticSensor(self):
    #    while True:
    #        if GPIO.input(8):
    #           print("Door is open")
    #           time.sleep(1)
    #        if GPIO.input(8) == False:
    #           print("Door is closed")
    #           time.sleep(1)
    def setMagnetic_open(self):
        self.magneticState = True

    def setMagnetic_close(self):
        self.magneticState = False

    def runMagneticSensor(self):
        while True:
            print("Hello")
            time.sleep(1)

if __name__ == "__main__":
    mag = clsMagneticSensor()
    mag.runMagneticSensor()