import time
from say import texttospeech

def countdown_timer():
    global setTimer

    texttospeech("Duration of Timer")
    setTimer = int(input("Duration of Timer (in minutes): ")) * 60
    texttospeech("Timer has been set, will inform you when the timer ends!")

    for i in range(setTimer, -1, -1):
        minutes, seconds = divmod(i, 60)
        #print(f"{minutes:02}:{seconds:02}")
        time.sleep(1)

    texttospeech("Your Timer has been completed")
    print("Your Timer has been completed")
