"""
class representing main controller for handling requests.
"""

from typing import Union
from fastapi import FastAPI

class mainApi:
    app = FastAPI()

    @app.get("/")
    def read_root(self):
        return {"Hello": "World"}

    @app.get("/items/{item_id}")
    def read_item(self, item_id: int, q: Union[str, None] = None):
        return {"item_id": item_id, "q": q}