"""
class representing main controller for handling requests.
"""
import shutil

from fastapi import APIRouter, Request, File, UploadFile, Body
from pydantic import BaseModel


import json
from .cloud import Cloud
from .audioProcessor import Processor
from .fileLoader import Loader
from .database import Database
from .requestHandlerer import ReqHendlerer
from ast import literal_eval

# setting path


class MainController:
    router = APIRouter()

    def __init__(self, jsonProcessor, loader, handler, audioProcessor):
        self.initRouters()
        self.jProcessor = jsonProcessor
        self.loader = loader
        self.handler = handler
        self.audioProcessor = audioProcessor
        self.db = Database('users', 'eu-west-1', '', '')
        self.db.connect()
        self.cloud = Cloud('aimtechackathon-mp3s', 'eu-west-1', '', '')
        self.cloud.connect()
        self.arr = []


    def getAudioMetadata(self):
        f = open("output.json")
        data = json.load(f)
        f.close()
        return data

    async def postRequest(self, request: Request):
        request = await request.json()
        self.db.put_item(request)

    def upload(self, file: UploadFile = File(...)):
        file_location = f"files/{file.filename}"
        with open(file_location, "wb+") as file_object:
            file_object.write(file.file.read())

        self.init(file_location)

        return {"200": "OK"}

    async def uploadText(self, request: Request):
        data = await request.json()

        data = json.dumps(data)

        with open("files/test.txt", "w+") as f:
            f.write(data)

        self.init("files/test.txt")


    def init(self, name):
        self.loader = Loader(name)
        data = self.loader.loadData()

        self.handler = ReqHendlerer(data)
        self.handler.call()

        self.audioProcessor = Processor(self.jProcessor)

        self.audioProcessor.beta()
        self.audioProcessor.getJoinedAudio()

    def getAudio(self):
        f = open("beta.mp3", "rb")
        return f.readlines()


    def initRouters(self):
        self.router.add_api_route("/audio", self.getAudioMetadata, methods=["GET"], status_code=200)
        self.router.add_api_route("/user", self.postRequest, methods=["POST"], status_code=200)
        self.router.add_api_route("/upload", self.upload, methods=["POST"], status_code=200)
        self.router.add_api_route("/getAudio", self.getAudio, methods=["GET"], status_code=200)
        self.router.add_api_route("/uploadText", self.uploadText, methods=["POST"], status_code=200)

