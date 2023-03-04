from json import JSONEncoder


class JsonProcessor(JSONEncoder):

    def default(self, o):
        return o.__dict__