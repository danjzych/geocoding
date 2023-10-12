# import geocoder library
from geopy.geocoders import Nominatim
# import distance measuring method
from geopy import distance

# instantiate geolocater - user agent is to let the creator know who is using
geolocator = Nominatim(user_agent="learning_how_toUse")

# can get addresses based on partial address - Willis tower Chi
a = geolocator.geocode("233 S Wacker Dr, Chicago")

# Memorial Union, Univiersity of Wisconsin
b = geolocator.geocode('800 Langdon St 53703')

# get distance
dist = distance.distance((a.latitude, a.longitude),
                         (b.latitude, b.longitude)).miles

print(dist)
