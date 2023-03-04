"""
class representing main controller for handling requests.
"""
from fastapi import APIRouter, Request, File, UploadFile
from pydantic import BaseModel

import sys

# setting path
sys.path.append('../app')
# importing
from utils.database import Database
from utils.cloud import Cloud


class MainController:
    router = APIRouter()

    def __init__(self, jProcessor, metadata):
        self.initRouters()
        self.jProcessor = jProcessor
        self.metadata = metadata
        self.db = Database('users', 'eu-west-1', 'AKIAZW5Y5IATVYH5VLH7', '31rrl9bQQe+aRv6h+4i/NZbVVF2WAcoslgkU08y6')
        self.db.connect()
        self.cloud = Cloud('aimtechackathon-mp3s', 'eu-west-1', 'AKIAZW5Y5IATVYH5VLH7', '31rrl9bQQe+aRv6h+4i/NZbVVF2WAcoslgkU08y6')
        self.cloud.connect()

    def getAudioMetadata(self):
        return self.metadata

    async def postRequest(self, request: Request):
        request = await request.json()
        self.db.put_item(request)

    async def uploadFile(self, file: UploadFile = File(...)):
        try:
            contents = file.file.read()
            # fo = io.BytesIO(b'my data stored as file object in RAM')
            # with open(file.filename, 'wb') as f:
            self.cloud.upload(contents)
        except Exception:
            return {"error": "There was an error uploading the file"}
        finally:
            file.file.close()
        return {"success": f"Successfully uploaded {file.filename}"}


    def initRouters(self):
        self.router.add_api_route("/audio", self.getAudioMetadata, methods=["GET"], status_code=200)
        self.router.add_api_route("/user", self.postRequest, methods=["POST"], status_code=200)
        self.router.add_api_route("/upload", self.uploadFile, methods=["POST"], status_code=200)

    # @router.post("/dummypath", status_code=201)
    # async def dummy(self, name: str = Body(...), price: float = Body(...)):
    #     return f"name {}"