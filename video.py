import pywhatkit as kit
from say import texttospeech

#Creating function to play youtube video or search
def video():
    texttospeech("What video would you like me to play")
    video = input("What video would you like me to play: ")
    texttospeech("Certainly, enjoy the video")
    kit.playonyt(video)