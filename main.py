#!/usr/bin/env python
# from loadfile import RadioUploader
# from deletefile import RadioCleaner

from flask import Flask
from flask import Response
from stream import Stream
from stream import ChunkManager
# from gevent.pywsgi import WSGIServer

import ConfigParser


app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route('/station/')
def index():
    # station index
    return ''

@app.route('/station/<string:name>')
def station(name):
    url = app.config["URLS"][name]
    stream = Stream( # TODO
        url= url,
        cm = ChunkManager('./data/', url)
    ).listen(60)

    return Response(stream, mimetype='audio/mpeg')


if __name__ == "__main__":
    config = ConfigParser.ConfigParser()
    config.read('./config.cfg')

    stations = config.sections()
    stations.remove('global')
    urls = {}
    for station in stations:
        urls[station] = config.get(station, 'url')

    app.config['URLS'] = urls
    # http_server = WSGIServer(('0.0.0.0', 5000), app)
    # http_server.serve_forever()
    app.run(host="0.0.0.0", threaded = True)
