from datetime import date
from say import texttospeech
from datetime import datetime

#Creating function to check date
def date():
    today = datetime.now().date().strftime('%m/%d/%y')
    texttospeech(today)
    print(today)
    