from pydub import AudioSegment
from modules.app.utils.utils import preprocess_words
# Load the audio file
pauza = AudioSegment.from_mp3("1secpause.mp3")
concated = None
text = "V dnešní den bude velmi zataženo s teplotami blízko nuly. K večeru očekáváme sněžení a mrholení.".lower()
pause_length = 0.1
for word in preprocess_words(text):
    audio = AudioSegment.from_mp3(f"words/{word}.mp3")
    if concated is None:
        concated = audio
    else:
        concated += pauza[:len(pauza)*pause_length] + audio

# Speed up the audio by 1.5x
#new_audio = audio.speedup(playback_speed=1.5, chunk_size=150, crossfade=25)

# Export the new audio file
concated.export("concated.mp3", format="mp3")