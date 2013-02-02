
from flask import Flask, Response

app = Flask(__name__)

from data import RestaurantDatabase

restaurants = RestaurantDatabase(file('data.csv'))

JSON = 'text/json'

@app.route("/")
def status():
    return Response('OK', mimetype=JSON)


