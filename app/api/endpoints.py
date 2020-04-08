from fuzzywuzzy import fuzz
from PyDictionary import PyDictionary
from flask_restful import Resource
from flask import g
from app import FLASK_REQUEST_COUNT, FLASK_REQUEST_GAUGE, FLASK_REQUEST_LATENCY
import time

class WordMeaning(Resource):
    def get(self, word):
        request_latency = time.time() - g.request_start_time
        FLASK_REQUEST_LATENCY.labels("GET", word).observe(request_latency)
        FLASK_REQUEST_COUNT.labels("GET", word, 200).inc()
        FLASK_REQUEST_GAUGE.labels("GET", "WordMeaningGauge").inc()
        dictionary = PyDictionary()
        return dictionary.meaning(word), 200

class MatchWords(Resource):
    def get(self, word1, word2):
        request_latency = time.time() - g.request_start_time
        FLASK_REQUEST_LATENCY.labels("GET", "MatchWordsEndPoint").observe(request_latency)
        FLASK_REQUEST_COUNT.labels("GET", "MatchWordsEndPoint", 200).inc()
        FLASK_REQUEST_GAUGE.labels("GET", "MatchWordsGauge").inc()
        return fuzz.ratio(word1, word2), 200

