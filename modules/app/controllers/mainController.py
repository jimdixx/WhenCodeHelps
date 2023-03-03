"""
class representing main controller for handling requests.
"""
from fastapi import APIRouter

class MainController:
    router = APIRouter()

    def __init__(self, jProcessor):
        self.initRouters()
        self.jProcessor = jProcessor

    def mainContent(self):
        return self.jProcessor.jsonOutput({"key1" : "val1", "key2": 3})

    def initRouters(self):
        self.router.add_api_route("/", self.mainContent, methods=["GET"])