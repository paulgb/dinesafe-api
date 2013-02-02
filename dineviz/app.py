
import cherrypy

from data import RestaurantDatabase

class APIServer(object):
    def __init__(self, restaurants):
        self.restaurants = restaurants

    @cherrypy.expose
    @cherrypy.tools.json_out()
    def getrange(self, limit=4):
        return list(range(int(limit)))

    @cherrypy.expose
    @cherrypy.tools.json_out()
    def index(self):
        return 'OK'

    @cherrypy.expose
    @cherrypy.tools.json_out()
    def random(self):
        return self.restaurants.random()

    @cherrypy.expose
    @cherrypy.tools.json_out()
    def near(self, lat, lon, n=10):
        lat = float(lat)
        lon = float(lon)
        n = int(n)
        return restaurants.find_nearest(lat, lon, n)

if __name__ == '__main__':
    DATA_FILE = 'sample.csv'
    restaurants = RestaurantDatabase()
    restaurants.load_csv(file(DATA_FILE))

    cherrypy.server.socket_host = '0.0.0.0'
    cherrypy.quickstart(APIServer(restaurants))

app = Flask(__name__)

