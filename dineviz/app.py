
from flask import Flask, Response

app = Flask(__name__)

#DATA_FILE = 'data.csv'
DATA_FILE = 'sample.csv'

from data import RestaurantDatabase
from jsonapi import json_endpoint

restaurants = RestaurantDatabase(file(DATA_FILE))

@app.route("/")
@json_endpoint
def status():
    return 'OK'

@app.route('/random')
@json_endpoint
def random():
    return restaurants.random()

