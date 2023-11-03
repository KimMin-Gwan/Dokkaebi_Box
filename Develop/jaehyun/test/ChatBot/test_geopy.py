
from geopy.geocoders import Nominatim

def geocoding(address):
    geolocoder = Nominatim(user_agent = 'South Korea', timeout=None)
    geo = geolocoder.geocode(address)
    crd = {"lat": str(geo.latitude), "lng": str(geo.longitude)}
    
    return crd


try:
    crd = geocoding('세빛섬')
    print(crd['lat'])
    print(crd['lng'])
except:
    print('주소가 잘못됨')
#crd = geocoding("서울역")
#crd = geocoding("동대구역")
#crd = geocoding("영남대")

#print(crd['lat'])
#print(crd['lng'])