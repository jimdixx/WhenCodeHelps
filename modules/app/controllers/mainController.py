"""
class representing main controller for handling requests.
"""
from fastapi import APIRouter, Request, Body

class MainController:
    router = APIRouter()

    def __init__(self, jProcessor, metadata):
        self.initRouters()
        self.jProcessor = jProcessor
        self.metadata = metadata

    def getAudioMetadata(self):
        return self.metadata

    def postRequest(self, username):
        return {"user": username}

    def initRouters(self):
        self.router.add_api_route("/audio", self.getAudioMetadata, methods=["GET"])
        self.router.add_api_route("/user/{username}", self.postRequest, methods=["GET"])

    # @router.post("/dummypath", status_code=201)
    # async def dummy(self, name: str = Body(...), price: float = Body(...)):
    #     return f"name {}"