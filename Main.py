import geopy as geopy


from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

from geopy.geocoders import Nominatim



def get_coordinates(country_name):
    geolocator = Nominatim(user_agent="MEC2020")
    location = geolocator.geocode(country_name)
    return location.latitude, location.longitude






def read(file):
    x = open(file, mode='r')
    y = x.readlines()
    return y


app = QApplication([])

world_map = QLabel()
map_data = QPixmap('World_Map_1.svg')
world_map.setPixmap(map_data)
world_map.show()


class MouseTracker(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.setMouseTracking(True)
    def initUI(self):

app.exec()


