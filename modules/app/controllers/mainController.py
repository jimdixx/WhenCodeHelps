"""
class representing main controller for handling requests.
"""
import sys
sys.path.append("..")

from fastapi import APIRouter

class MainController:
    router = APIRouter()

    def __init__(self):
        self.initRouters()

    def mainContent(self):
        return {"content": "content"}

    def initRouters(self):
        self.router.add_api_route("/", self.mainContent, methods=["GET"])