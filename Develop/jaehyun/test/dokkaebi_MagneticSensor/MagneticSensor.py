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
from dokkaebi_MagneticSensor.magneticConstant import *

class dokkaebi_Magneticsensor:
    def __init__(self, dokkaebi_Rasp_Cam, dokkaebi_Rasp_Servo):
        self.dokkaebi_Rasp_Cam = dokkaebi_Rasp_Cam
        self.dokkaebi_Rasp_Servo = dokkaebi_Rasp_Servo
        GPIO.setmode(GPIO.BOARD)
        #GPIO.setup(MAGNETIC_DEFAULT_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.setup(MAGNETIC_DEFAULT_PIN, GPIO.IN)
        self.magneticDoorState = False # False(닫힘)/True(열림)

    def setMagnetic_open(self):
        self.magneticDoorState = True

    def setMagnetic_close(self):
        self.magneticDoorState = False

    def getMagneticDoorState(self):
        return

    def runMagneticSensor(self):
        
        while True:
            if GPIO.wait_for_edge(MAGNETIC_DEFAULT_PIN, GPIO.RISING, bouncetime=300) == MAGNETIC_DEFAULT_PIN:
                self.setMagnetic_close()
                self.dokkaebi_Rasp_Cam.run_Camera()
                self.dokkaebi_Rasp_Servo.closeDoor()
                print("SYSTEM MESSAGE::The door closed")
            if GPIO.wait_for_edge(MAGNETIC_DEFAULT_PIN, GPIO.FALLING, bouncetime=300) == MAGNETIC_DEFAULT_PIN:
                #self.dokkaebi_Rasp_Servo.openDoor()
                print("SYSTEM MESSAGE::The door opened")

        #while True:
        #    if GPIO.input(MAGNETIC_DEFAULT_PIN) == GPIO.HIGH:
        #        self.setMagnetic_close()
        #        self.dokkaebi_Rasp_Cam.run_Camera()
        #        self.dokkaebi_Rasp_Servo.closeDoor()
        #        print("SYSTEM MESSAGE::The door closed")
        #    elif GPIO.input(MAGNETIC_DEFAULT_PIN) == GPIO.LOW:
        #        self.dokkaebi_Rasp_Servo.openDoor()
        #        print("SYSTEM MESSAGE::The door opened")


