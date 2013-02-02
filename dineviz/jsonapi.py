
import json
from functools import wraps

from flask import Response

JSON = 'text/json'

def jsonify(obj):
    return json.dumps(obj, sort_keys=True, indent=4, separators=(',', ':'))

def json_endpoint(func):
    @wraps(func)
    def outputs_json(*args, **kwargs):
        result = func(*args, **kwargs)
        return Response(jsonify(result), mimetype=JSON)
    return outputs_json

