#Importing TextToSpeech and Time
from say import texttospeech
import time

#Creating loading message function
def loadMessage():
    print("Activating Voice Recognition ...")
    texttospeech("Activating Voice Recognition ...")
    time.sleep(0.02)

    print("Importing Weather Details ...")
    texttospeech("Importing Weather Details ...")
    time.sleep(0.02)

    print("Enabling All Functions ...")
    texttospeech("Enabling All Functions ...")
