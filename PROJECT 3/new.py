import phonenumbers
from phonenumbers import geocoder
import folium
import opencage

number ="+91 1126514829"
Key="de7d80cb4ebd4c1f9395eaa68a87b807"

check_number = phonenumbers.parse(number)
number_location= geocoder.description_for_number(check_number, 'en')
print(number_location)

from phonenumbers import carrier
service_provider = phonenumbers.parse(number)
print(carrier.name_for_number(service_provider, "en"))

from opencage.geocoder import OpenCageGeocode
geocoder = OpenCageGeocode(Key)

query = str(number_location)
results = geocoder.geocode(query)

lat = results[0]['geometry']['lat']
lng = results[0]['geometry']['lng']
print(lat, lng)

map_location = folium.Map(location = [lat,lng], zoom_start=10)
folium.Marker([lat, lng], popup=number_location).add_to(map_location)
map_location.save("mylocation.html")