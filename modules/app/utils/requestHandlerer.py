from requests.auth import HTTPDigestAuth
import requests
import time

class ReqHendlerer:

    ROOT = "https://services.speechtech.cz/tts/v4"
    USERNAME = "aimtechackathon"
    PASSWORD = "lu7Eabuu7E"
    DELAY = 0.3

    def __init__(self, arr):
        self.arr = arr
        self.processed = []

    def call(self):
        id = 0
        for text in self.arr:
            r = requests.get(self.ROOT + "/synth",
                             data={"engine": "Iva30",  # Iva30, Jan30
                                   "text": text,
                                   "format": "mp3",
                                   },
                             auth=HTTPDigestAuth(self.USERNAME, self.PASSWORD),
                             )
            r.raise_for_status()

            with open("fetched/output_" + str(id) + ".mp3", "wb") as fw:
                fw.write(r.content)
            id += 1

