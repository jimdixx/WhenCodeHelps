"""
Main class which starts its server (mainly
"""
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from utils.mainController import MainController
from utils.jsonProcessor import JsonProcessor
from utils.fileLoader import Loader
from utils.requestHandlerer import ReqHendlerer
from utils.audioProcessor import Processor

app = FastAPI()


origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


jsonProcessor = JsonProcessor()
loader = Loader()
handler = ReqHendlerer()
audioProcessor = Processor()


# HANDLING API REQUESTS
mainController = MainController(jsonProcessor, loader, handler, audioProcessor)
app.include_router(mainController.router)