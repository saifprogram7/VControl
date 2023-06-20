#Importing TextToSpeech, DateTime, LoadMessage
from say import texttospeech
from datetime import datetime
from loadingmessage import loadMessage

#Creating Funciton called user
def user():
    currentTime = datetime.now().hour
    if (currentTime >= 6) and (currentTime <= 11):
        texttospeech("Good Morning sir")
        loadMessage()
    elif (currentTime >= 11) and (currentTime <= 15):
        texttospeech("Good Afternoon sir")
        loadMessage()
    elif (currentTime >= 16) and (currentTime <= 18):
        texttospeech("Good Evening sir")
        loadMessage()
    elif (currentTime >= 19) and (currentTime <= 21):
        texttospeech("Sir please have your dinner")
        loadMessage()
    elif (currentTime >= 21) and (currentTime <= 23):
        texttospeech("Sir it is getting too late")
        loadMessage()
    elif (currentTime >=0) and (currentTime < 6):
        texttospeech("Sir please go to bed")
