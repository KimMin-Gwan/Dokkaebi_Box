
# Server constant
UDP_IP="172.30.1.2"  #서버(사진 전달할)  주소
UDP_PORT=8000    #서버 (사진 전달할)   포트 번호
MAX_SEND_BYTES=5500
CAPTUR_IMAGE_NAME="output.jpg"


END_FLAG="end".encode()   #end flag

# Servo Constant
SERVO_DEFAULT_FREQ = 50 # Servo Motor는 50Hz(20ms) 사용
SERVO_DEFAULT_PIN = 12  # 라즈베리파이 GPIO 보드 기준 12번 Pin

SERVO_MAX_DUTY = 12   # 서보의 최대(180도) 위치의 주기
SERVO_MIN_DUTY = 3    # 서보의 최소(0도) 위치의 주기

# Magnetic Constant
MAGNETIC_DEFAULT_PIN = 10