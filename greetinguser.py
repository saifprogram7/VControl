from say import texttospeech
from datetime import datetime

def greet_user():
    hour = datetime.now().hour
    if (hour >= 6) and (hour < 12):
        texttospeech("Good Morning Sir")
    elif (hour >= 12) and (hour < 16):
        texttospeech("Good afternoon Sir")
    elif (hour >= 16) and (hour < 19):
        texttospeech("Good Evening Sir")
    elif (hour >=19) and (hour < 24):
        texttospeech("Hello sir")