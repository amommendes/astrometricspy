from fuzzywuzzy import fuzz
from PyDictionary import PyDictionary
from flask_restful import Resource

class WordMeaning(Resource):
    def get(self, word):
        dictionary = PyDictionary()
        return dictionary.meaning(word), 200

class MatchWords(Resource):
    def get(self, word1, word2):
        return fuzz.ratio(word1, word2), 200

