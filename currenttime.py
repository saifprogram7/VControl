from say import texttospeech
from datetime import datetime

#Creating function to check date
def time():
    todaytime = datetime.now().time().strftime('%H:%M')
    texttospeech(todaytime)
    print(todaytime)