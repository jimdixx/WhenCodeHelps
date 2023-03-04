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


from requests.auth import HTTPDigestAuth
import requests

ROOT = "https://services.speechtech.cz/tts/v4"
USERNAME = "aimtechackathon"
PASSWORD = "lu7Eabuu7E"

r = requests.get(ROOT+"/synth",
                 data={"engine": "Iva30",  # Iva30, Jan30
                       "text": "Toto. je. verze. kterou. chci. zpomalit.",
                       "format": "mp3",
                       },
                  auth=HTTPDigestAuth(USERNAME, PASSWORD),
                 )
r.raise_for_status()

with open("output.mp3", "wb") as fw:
    fw.write(r.content)


from pydub import AudioSegment

# Load the MP3 file
audio = AudioSegment.from_file("output.mp3", format="mp3")

# Slow down the audio by a factor of 0.75
slow_audio = audio._spawn(audio.raw_data, overrides={
    "frame_rate": int(audio.frame_rate * 0.90)
})
slow_audio = slow_audio.set_frame_rate(audio.frame_rate)

# Export the slowed down audio to a new MP3 file
slow_audio.export("output-slowed.mp3", format="mp3")


