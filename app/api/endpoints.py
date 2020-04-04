from fuzzywuzzy import fuzz
from PyDictionary import PyDictionary
from flask_restful import Resource
from app import FLASK_REQUEST_COUNT, FLASK_REQUEST_GAUGE

class WordMeaning(Resource):
    def get(self, word):
        FLASK_REQUEST_COUNT.labels('GET', 'WordMeaning', 200).inc()
        FLASK_REQUEST_GAUGE.labels("GET", "WordMeaning").inc()
        dictionary = PyDictionary()
        return dictionary.meaning(word), 200

class MatchWords(Resource):
    def get(self, word1, word2):
        return fuzz.ratio(word1, word2), 200

