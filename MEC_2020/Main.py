import geopy as geopy

from geopy.geocoders import Nominatim
import matplotlib.pyplot as plt

def get_coordinates(country_name):
    geolocator = Nominatim(user_agent="MEC2020")
    location = geolocator.geocode(country_name)
    return location.latitude, location.longitude


def draw_map():
    img = plt.imread()
