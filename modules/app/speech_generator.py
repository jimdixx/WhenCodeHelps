from requests.auth import HTTPDigestAuth
import requests
from utils import preprocess_words

ROOT = "https://services.speechtech.cz/tts/v4"
USERNAME = "aimtechackathon"
PASSWORD = "lu7Eabuu7E"


def get_word(word):
    r = requests.get(ROOT + "/synth",
                     data={"engine": "Iva30",  # Iva30, Jan30
                           "text": word,
                           "format": "mp3",
                           },
                     auth=HTTPDigestAuth(USERNAME, PASSWORD),

                     )
    r.raise_for_status()

    with open(f"words/{word.lower()}.mp3", "wb") as fw:
        fw.write(r.content)


text = "V dnešní den bude velmi zataženo s teplotami blízko nuly. K večeru očekáváme sněžení a mrholení.".lower()

for word in preprocess_words(text):
        get_word(word)


