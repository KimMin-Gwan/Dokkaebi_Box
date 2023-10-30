"""
* Project : 2023 Seoul AIOT Hackathon
* Program Purpose and Features :
* - class ServoMotor constant
* Author : JH KIM
* First Write Date : 2023.11.03
* ==========================================================================
* Program history
* ==========================================================================
* Author    		Date		    Version		History
* JH KIM            2023.11.03		v1.00		First Write
"""
SERVO_DEFAULT_FREQ = 50 # Servo Motor는 50Hz(20ms) 사용
SERVO_DEFAULT_PIN = 12  # 라즈베리파이 GPIO 보드 기준 12번 Pin

SERVO_MAX_DUTY = 12   # 서보의 최대(180도) 위치의 주기
SERVO_MIN_DUTY = 3    # 서보의 최소(0도) 위치의 주기