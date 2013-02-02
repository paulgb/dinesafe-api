
import json
from functools import wraps

from flask import Response
import cherrypy

JSON = 'text/json'

def jsonify(obj):
    return json.dumps(obj, sort_keys=True, indent=4, separators=(',', ':'))

