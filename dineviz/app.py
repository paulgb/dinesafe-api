
from flask import Flask, Response
app = Flask(__name__)

JSON = 'text/json'

@app.route("/")
def status():
    return Response('OK', mimetype=JSON)

if __name__ == "__main__":
    app.run()

