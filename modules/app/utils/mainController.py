"""
class representing main controller for handling requests.
"""
import shutil
import openai
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
# GPT-3 API anahtarınızı kullanarak OpenAI API'yi yapılandırın
openai.api_key = "APIKEY-XXXX"

def generate_response(prompt):
  completions = openai.Completion.create(
      engine="text-davinci-003",
      prompt="Zjednodusi nasledujici text: \"" + prompt + "\"",
      max_tokens=1024,
      n=1,
      stop=None,
      temperature=0.5,
  )

  message = completions.choices[0].text
  return message


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

        if data["simplify"]:
            data["text"] = generate_response(data["text"])

        data = json.dumps(data, ensure_ascii = False)

        with open("files/test.txt", "w+") as f:
            f.write(data)

        self.init("files/test.txt")

        return {"200": "OK"}

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
        return f.read()


    def initRouters(self):
        self.router.add_api_route("/audio", self.getAudioMetadata, methods=["GET"], status_code=200)
        self.router.add_api_route("/user", self.postRequest, methods=["POST"], status_code=200)
        self.router.add_api_route("/upload", self.upload, methods=["POST"], status_code=200)
        self.router.add_api_route("/getAudio", self.getAudio, methods=["GET"], status_code=200)
        self.router.add_api_route("/uploadText", self.uploadText, methods=["POST"], status_code=200)

