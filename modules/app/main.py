"""
Main class which starts its server (mainly
"""
from fastapi import FastAPI
from controllers.mainController import MainController
from utils.jsonProcessor import JsonProcessor
from utils.fileLoader import Loader
from utils.requestHandlerer import ReqHendlerer
from utils.audioProcessor import Processor

app = FastAPI()

jsonProcessor = JsonProcessor()



loader = Loader("test.txt")
data = loader.loadData()

handler = ReqHendlerer(data)
handler.call()

audioProcessor = Processor(jsonProcessor)

audioProcessor.beta()

# Getting array with metadata of slowed audio in .json format
arr = audioProcessor.getArrayWithJson()


# HANDLING API REQUESTS
mainController = MainController(jsonProcessor, arr)
app.include_router(mainController.router)