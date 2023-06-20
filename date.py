from say import texttospeech
from datetime import datetime

#Creating function to check date
def date():
    today = datetime.now().date()
    texttospeech(today)
    print(today)
    