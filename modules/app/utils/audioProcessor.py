from pydub import AudioSegment
import os


class Audio:
    def __init__(self, id, time):
        self.id = id
        self.time = time



class Processor:

    def __init__(self, jsonProcessor=None):
        self.json = jsonProcessor
        self.arr = []
        self.audio = None

    def beta(self):

        dir_list = os.listdir("fetched")
        dir_list.sort(key=lambda x: int(x.split("_")[1].split(".mp3")[0]))

        id = 0
        for mp3 in dir_list:

            FILE_PATH = "fetched/" + mp3

            # Load the MP3 file
            audio = AudioSegment.from_file(FILE_PATH, format="mp3")

            audioDto = Audio(id, audio.duration_seconds)
            self.arr.append(self.json.encode(audioDto))

            # Slow down the audio by a factor of 0.75
            slow_audio = audio._spawn(audio.raw_data, overrides={
                "frame_rate": int(audio.frame_rate * 0.95)
            })
            slow_audio = slow_audio.set_frame_rate(audio.frame_rate)

            if id == 0:
                self.audio = slow_audio
            else:
                self.audio += slow_audio

            os.remove(FILE_PATH)

            id += 1
        with open("output.json", "w+") as f:
            f.write(self.json.encode(self.arr))


    def getArrayWithJson(self):
        return self.arr

    def getJoinedAudio(self):
        self.audio.export("static/beta.mp3", format="mp3")
