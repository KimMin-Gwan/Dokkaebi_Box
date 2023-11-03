SAVE_IMAGE_PATH="C:\\Users\\maths\\Desktop\\한강IOT사진\\" 
UDP_IP = "172.30.1.2"  #내 ip주소
UDP_PORT = 8888
END_FLAG="end".encode()
MAX_SEND_BYTES=10000

#####데이터 베이스 key값 정리 

CLASSIFICATION="classification"   #분류 말 그대로 cellphone wallet etc등등
LAT="let"  #위도
LNG="lng"  #경도
DATE="date"   #분실한 날짜
LOSTPLACE="lostplace"  #분실한 장소 
LOSTTIME="losttime"  #분실한 시간 
PATH="path"  #이미지 저장 path 
PWD="password"

STATE="state"  #인계하는지 아니면 박스인지

MONGODB_ADDR="mongodb+srv://sunjuwhan:ans693200@sunjuwhan.soaegl1.mongodb.net/"
CLIENT_LOC="IOT"   #상위
DB_LOC="image"  #하위 폴더