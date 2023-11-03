"""
* Project : 2023 Seoul AIOT Hackathon
* Program Purpose and Features :
* - class dokkaebi_Servo
* Author : JH KIM
* First Write Date : 2023.11.03
* ==========================================================================
* Program history
* ==========================================================================
* Author    		Date		    Version		History
* JH KIM            2023.11.03		v1.00		First Write
"""
import RPi.GPIO as GPIO
import time

from dokkaebi_Servo.ServoConstant import *


class dokkaebi_Servo:
    def __init__(self):
        GPIO.setwarnings(False)
        self.pin = SERVO_DEFAULT_PIN
        self.nowDegree = 0
        GPIO.setmode(GPIO.BOARD)    # 핀의 번호를 보드 기준으로 설정, BCM은 GPIO 번호로 호출함
        GPIO.setup(self.pin, GPIO.OUT)   # GPIO 통신할 핀 설정
        self.pwm = GPIO.PWM(self.pin, SERVO_DEFAULT_FREQ)  # 서보모터는 PWM을 이용해야됨. 16번핀을 50Hz 주기로 설정
        self.pwm.start(0)   # 초기 시작값 0도, 반드시 입력해야됨
        time.sleep(1)       # 초기 시작값으로 이동하고 싶지 않으면 이 라인을 삭제하면 된다.


    def setNowDegree(self, deg):
        self.nowDegree = deg

    def getNowDegree(self):
        return self.nowDegree

    def setDegree(self, degree, t):   # 각도와 움직일 시간 입력
        self.setNowDegree(degree)
        duty = SERVO_MIN_DUTY + ((degree * (SERVO_MAX_DUTY - SERVO_MIN_DUTY) / 180.0))*1.15 # 1.15는 서보모터 특성에 따른 보정값
        self.pwm.ChangeDutyCycle(duty)  # 보통 2~12 사이의 값을 입력하면됨
        time.sleep(t)  # 서보모터가 이동할만큼의 충분한 시간을 입력. 너무 작은 값을 입력하면 이동하다가 멈춤

    def closeDoor(self):
        self.setDegree(90, 0.7)
        self.setNowDegree(90)

    def openDoor(self):
        self.setDegree(0, 0.7)
        self.setNowDegree(90)
def main():
    servo = dokkaebi_Servo()
    while True:
        servo.setDegree(0, 1) # 0도
        servo.setDegree(90, 1)  # 90도
if __name__ == "__main__":
    main()
