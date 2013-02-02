
import cherrypy

from data import RestaurantDatabase
from jsonapi import json_api
from jinja2 import Template

class APIServer(object):
    def __init__(self, restaurants):
        self.restaurants = restaurants
        self.info_template = Template(file('info.html').read())

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

    @json_api
    def fuzzy_match(self, lat, lon, name):
        lat = float(lat)
        lon = float(lon)
        return restaurants.find_fuzzy(lat, lon, name)

    @json_api
    def all(self):
        return restaurants.all()

    @cherrypy.expose
    def info(self, id):
        restaurant = restaurants.find_by_id(long(id))
        return self.info_template.render(restaurant=restaurant)

if __name__ == '__main__':
    DATA_FILE = 'data.csv'
    restaurants = RestaurantDatabase()
    restaurants.load_csv(file(DATA_FILE))

    cherrypy.server.socket_host = '0.0.0.0'
    cherrypy.quickstart(APIServer(restaurants))

