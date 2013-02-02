
import cherrypy

from data import RestaurantDatabase
from jsonapi import json_api

class APIServer(object):
    def __init__(self, restaurants):
        self.restaurants = restaurants

    @json_api
    def index(self):
        return 'OK'

    @json_api
    def random(self):
        return self.restaurants.random()

    @json_api
    def near(self, lat, lon, n=10):
        lat = float(lat)
        lon = float(lon)
        n = int(n)
        return restaurants.find_nearest(lat, lon, n)

    @json_api
    def establishment(self, id):
        id = long(id)
        return restaurants.find_by_id(id)

if __name__ == '__main__':
    DATA_FILE = 'data.csv'
    restaurants = RestaurantDatabase()
    restaurants.load_csv(file(DATA_FILE))

    cherrypy.server.socket_host = '0.0.0.0'
    cherrypy.quickstart(APIServer(restaurants))

app = Flask(__name__)

