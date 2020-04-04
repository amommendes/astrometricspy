import os
from flask import Flask, request, g
from flask_restful import Api
from prometheus_client import start_http_server, Counter, Histogram, Gauge
import time

FLASK_REQUEST_COUNT = Counter('flask_request_counter', 'Flask Request Count', ['method', 'endpoint', 'http_status'])
FLASK_REQUEST_LATENCY = Histogram('flask_request_latency_seconds', 'Flask Request Latency', ['method', 'endpoint'])
FLASK_REQUEST_GAUGE = Gauge('flask_gauge_metric', 'Flask Gauge', ['method', 'endpoint'])

def before_request_func():
    g.request_start_time = time.time()

def after_request(response):
        print("Before request!")
        request_latency = time.time() - g.request_start_time
        FLASK_REQUEST_LATENCY.labels(request.method, request.path).observe(request_latency)
        FLASK_REQUEST_COUNT.labels(request.method, request.path, response.status_code).inc()
        FLASK_REQUEST_GAUGE.labels(request.method, request.path).inc()
        return response

def create_app(test_config=None):

    app = Flask(__name__, instance_relative_config=False)
    app.config.from_pyfile("instance/config.py")
    app.config.from_mapping(SECRET_KEY='dev')

    api = Api(app)
    app.before_request(before_request_func)
    app.after_request(after_request)
    try:
        print( "I'm using 9001" )
        start_http_server(9001)
    except OSError as error:
        print("It seems that port is already in use {}".format(error))
        start_http_server(9001+1)


    if test_config is None:
        # load the instance instance, if it exists, when not testing
        app.config.from_pyfile('instance/config.py', silent=True)
    else:
        # load the test instance if passed in
        app.config.from_mapping(test_config)

    from app.api import endpoints
    api.add_resource(endpoints.WordMeaning, "/words/meaning/<word>",)
    api.add_resource(endpoints.MatchWords, "/words/match/<word1>/<word2>",)

    @app.route('/stats', methods=['GET'])
    def metrics():
        return generate_latest(registry), 200

    return app