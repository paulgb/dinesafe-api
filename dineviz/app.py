
from flask import Flask, Response, request

app = Flask(__name__)

#DATA_FILE = 'data.csv'
DATA_FILE = 'sample.csv'

from data import RestaurantDatabase
from jsonapi import json_endpoint

restaurants = RestaurantDatabase()
restaurants.load_csv(file(DATA_FILE))

@app.route("/")
@json_endpoint
def status():
    return 'OK'

@app.route('/random')
@json_endpoint
def random():
    return restaurants.random()

@app.route('/near')
@json_endpoint
def near():
    lat = float(request.args['lat'])
    lon = float(request.args['lon'])
    n = int(request.args.get('n', 10))
    return restaurants.find_nearest(lat, lon, n)

