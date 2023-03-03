"""
Main class which starts its server (mainly
"""
from fastapi import FastAPI
from controllers.mainController import MainController


app = FastAPI()
mainController = MainController()
app.include_router(mainController.router)

