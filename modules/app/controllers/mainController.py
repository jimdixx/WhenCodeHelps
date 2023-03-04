"""
class representing main controller for handling requests.
"""
from fastapi import APIRouter, Request
from pydantic import BaseModel

import sys

# setting path
sys.path.append('../app')
# importing
from utils.database import Database



class MainController:
    router = APIRouter()

    def __init__(self, jProcessor, metadata):
        self.initRouters()
        self.jProcessor = jProcessor
        self.metadata = metadata
        self.db = Database('users', 'eu-west-1', 'AKIAZW5Y5IATVYH5VLH7', '31rrl9bQQe+aRv6h+4i/NZbVVF2WAcoslgkU08y6')
        self.db.connect()

    def getAudioMetadata(self):
        return self.metadata

    async def postRequest(self, request: Request):
        request = await request.json()
        self.db.put_item(request)

    def initRouters(self):
        self.router.add_api_route("/audio", self.getAudioMetadata, methods=["GET"], status_code=200)
        self.router.add_api_route("/user", self.postRequest, methods=["POST"], status_code=200)
        # self.router.add_api_route("/process", self.)

    # @router.post("/dummypath", status_code=201)
    # async def dummy(self, name: str = Body(...), price: float = Body(...)):
    #     return f"name {}"