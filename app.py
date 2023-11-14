# import geocoder library
from geopy.geocoders import Nominatim
# import distance measuring method
from geopy import distance

# instantiate geolocater - user agent is to let the creator know who is using
geolocator = Nominatim(user_agent="learning_how_toUse")


def get_distance(location_a, location_b):
    """Function for getting distance between geocoded addresses"""
    a = geolocator.geocode(f'{location_a}, USA')
    b = geolocator.geocode(f'{location_b}, USA')
    print(a)
    print(b)

    return round(distance.distance((a.latitude, a.longitude),
                                   (b.latitude, b.longitude)).miles, 0)


sears_tower = "233 S Wacker Dr, Chicago"

# can work off partial address as seen below
memorial_union = "800 Langdon St 53703"

print(get_distance(53704, 53701
                   ))
