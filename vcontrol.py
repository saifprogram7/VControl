from ip import ip
from word import word
from file import file
from date import date       
from video import video     
from vscode import code   
from folder import folder  
from chrome import chrome   
from discord import discord 
from website import website 
from standby import standby
from currenttime import time
from say import texttospeech 
from conversation import user
from cmdline import commandline
from powerpoint import powerpoint
from calculator import calculator
from timer import countdown_timer
from weather import weather_forcast
from streamlabsobs import streamlabsOBS
from information import informationAutomation

# Calling Conversation Function
user()

#Calling Weather Function
weather_forcast()

#Active for while loop
active = True

#Counter for while loop
counter = 0

#Features inside VControl
features = {"calculator", "cmd", "discord", "information", "chrome", "code", "video", "website", "date", "time", "folder", "file", "word",
            "streamlabs", "powerpoint", "countdown", "weather"}

while active:
    counter+= 1

    if counter > 1:
        texttospeech("Is there anything else I can assist you with?")
        repeat = input("Is there anything else I can assist you with: ").lower()

        if "stand by" in repeat:
            standby()
            counter = 0
            continue

        elif "no" in repeat:
            texttospeech("Enjoy the rest of your day!")
            break

    texttospeech("How may I be of service?")
    userChoice = input("How may I be of service: ").lower()

    if "features" in userChoice:
        texttospeech("The features I have available are")
        texttospeech(features)
        print(features)
        continue

    elif "calculator" in userChoice:
        texttospeech("Sure sir opening calculator now!")
        calculator()
        continue

    elif "cmd" in userChoice:
        texttospeech("Certainly sir opening command line now!")
        commandline()
        continue

    elif "discord" in userChoice:
        texttospeech("Absolutely sir opening discord now!")
        discord()
        continue

    elif "information" in userChoice:
        texttospeech("Sure sir, what information do you require?")
        requirement = input("What information do you require: ")
        texttospeech("I hope this website is useful!")
        informationAutomation(requirement)
        continue

    elif "chrome" in userChoice:
        texttospeech("Certainly sir opening google chrome now!")
        chrome()
        continue

    elif "code" in userChoice:
        texttospeech("Opening VS Code now sir!")
        code()
        continue

    elif "video" in userChoice:
        texttospeech("Sure sir")
        video()
        continue

    elif "website" in userChoice:
        texttospeech("Sure sir")
        website()
        continue

    elif "date" in userChoice:
        texttospeech("The current date is")
        date()
        continue
            
    elif "countdown" in userChoice:
        texttospeech("Sure sir")
        countdown_timer()
        continue

    elif "time" in userChoice:
        texttospeech("The current time is")
        time()
        continue

    elif "folder" in userChoice:
        texttospeech("Sure sir")
        folder()
        continue

    elif "file" in userChoice:
        texttospeech("Absolutely sir")
        file()
        continue

    elif "word" in userChoice:
        texttospeech("Opening word document now")
        word()
        continue

    elif "streamlabs" in userChoice:
        texttospeech("Opening up obs now sir")
        streamlabsOBS()
        continue

    elif "powerpoint" in userChoice:
        texttospeech("Opening up powerpoint now")
        powerpoint()
        continue

    elif "ip" in userChoice:
        ip()
        continue

    elif "weather" in userChoice:
        texttospeech("Certainly!")
        weather_forcast()
        continue

    elif "exit" in userChoice:
        texttospeech("Enjoy the rest of your day!")
        break

    elif "stand by" in userChoice:
        standby()
        counter = 0
        continue
    
    else:
        texttospeech("Sorry sir I do not have that feature available at the moment")
        counter = 0
        continue
