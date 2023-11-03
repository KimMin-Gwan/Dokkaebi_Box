
from geopy.geocoders import Nominatim
import mpu
def geocoding(address):
    geolocoder = Nominatim(user_agent = 'South Korea', timeout=None)
    geo = geolocoder.geocode(address)
    crd = {"lat": str(geo.latitude), "lng": str(geo.longitude)}
    
    return crd


try:
    crd = geocoding('한강')
    a=float(crd['lat'])
    b=float(crd['lng'])

    crd_2=geocoding('양화대교')
    a_2=float(crd_2['lat'])
    b_2=float(crd_2['lng'])

    crd_3=geocoding('마포대교')
    a_3=float(crd_3['lat'])
    b_3=float(crd_3['lng'])

    crd_4=geocoding('여의나루')
    a_4=float(crd_4['lat'])
    b_4=float(crd_4['lng'])

    crd_5=geocoding('여의나루')
    a_5=float(crd_5['lat'])
    b_5=float(crd_5['lng'])

except:
    print('주소가 잘못됨')



print(mpu.haversine_distance((a,b),(a_2,b_2)))
print(mpu.haversine_distance((a,b),(a_3,b_3)))
print(mpu.haversine_distance((a,b),(a_4,b_4)))
print(mpu.haversine_distance((a,b),(a_5,b_5)))




import math

def haversine(lat1, lon1, lat2, lon2):
    # 지구 반지름 (킬로미터)
    radius = 6371.0
    
    # 라디안으로 위도 경도 변환
    lat1 = math.radians(lat1)
    lon1 = math.radians(lon1)
    lat2 = math.radians(lat2)
    lon2 = math.radians(lon2)
    
    # Haversine 공식 계산
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = math.sin(dlat/2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon/2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    distance = radius * c
    
    return distance

def find_closest_points(data):
    min_distance = float('inf')
    closest_points = None

    for i in range(len(data)):
        for j in range(i + 1, len(data)):
            lat1, lon1 = data[i]
            lat2, lon2 = data[j]
            distance = haversine(lat1, lon1, lat2, lon2)

            if distance < min_distance:
                min_distance = distance
                closest_points = (data[i], data[j])

    return closest_points, min_distance

# 위도 경도 데이터 샘플
data = [(37.478875,126.982029),  (39.7835588,125.9429579)]

closest_points, min_distance = find_closest_points(data)
print("가장 가까운 두 점:", closest_points)
print("거리 (킬로미터):", min_distance)