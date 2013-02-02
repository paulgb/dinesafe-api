
from functools import wraps

import cherrypy

def json_api(fun):
    @cherrypy.expose
    @cherrypy.tools.json_out()
    @wraps(fun)
    def jsonified(*args, **kwargs):
        cherrypy.response.headers['Access-Control-Allow-Origin'] = '*'
        return fun(*args, **kwargs)
    return jsonified

