"""
Main class which starts its server (mainly
"""
from fastapi import FastAPI
from controllers.mainController import MainController
from utils.jsonProcessor import JsonProcessor

app = FastAPI()

jsonProcessor = JsonProcessor()

mainController = MainController(jsonProcessor)
app.include_router(mainController.router)

