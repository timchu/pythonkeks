from pydub import AudioSegment
from pydub.playback import play

def playSound(fname, volAmplifier = 0):
    timesound = AudioSegment.from_mp3(fname)
    ts = timesound + volAmplifier
    play(ts)
def playTimeSound():
    playSound("./sounds/time.mp3", 15)
