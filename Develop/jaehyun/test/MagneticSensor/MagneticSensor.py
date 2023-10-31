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
        GPIO.setup(MAGNETIC_DEFAULT_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        self.magneticState = False # False(닫힘)/True(열림)

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
            state = GPIO.wait_for_edge(MAGNETIC_DEFAULT_PIN, GPIO.FALLING, bouncetime=200)
            print("FALLING" + str(state))
            state = GPIO.wait_for_edge(MAGNETIC_DEFAULT_PIN, GPIO.RISING, bouncetime=200)
            print("RISING" + str(state))



if __name__ == "__main__":
    mag = clsMagneticSensor()
    mag.runMagneticSensor()