import json

class JsonProcessor:

    def jsonOutput(self, object):
        return json.JSONEncoder().encode(object)