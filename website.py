import webbrowser as wb
from say import texttospeech

#Creating function to open specific website
def website():
    texttospeech("What website would you like me to open?")
    websiteurl = input("What website would you like me to open: ").lower()

    #Creating IF statement to check if the user has typed 'google'
    if "google" in websiteurl:
        texttospeech("Sure sir, opening google now!")
        wb.open('www.google.com')

    #Creating ELIF statement to check if the user has typed 'youtube'    
    elif "youtube" in websiteurl:
        texttospeech("Absolutely sir, opening youtube now!")
        wb.open('www.youtube.com')

    #Creating ELIF statement to check if the user has typed 'aula'    
    elif "aula" in websiteurl:
        texttospeech("Certainly sir, opening study protal now!")
        wb.open('https://rave.aula.education/#/dashboard/d3d10d94-145a-47d7-8a15-993dee067d62/community/feed')
    
    #Creating ELIF statement to check if the user has typed 'teams'
    elif "teams" in websiteurl:
        texttospeech("Yes sir, opening microsoft teams now!")
        wb.open('https://teams.microsoft.com/_?culture=en-us&country=ww#/conversations/19:8a1e17c5-17b8-437d-88ab-96a73c79e0c0_be6addc1-1ab0-4fe2-aab0-da4773198b1f@unq.gbl.spaces?ctx=chat')
    
    #Creating ELIF statement to check if the user has typed 'tryhackme'
    elif "tryhackme" in websiteurl:
        texttospeech("All the best sir, opening try hack me now!")
        wb.open('https://tryhackme.com/dashboard')

    #Creating ELIF statement to check if the user has typed 'drive'
    elif "drive" in websiteurl:
        texttospeech("Sure sir, opening google drive now!")
        wb.open('https://drive.google.com/drive/u/0/my-drive')

    #Creating ELIF statement to check if the user has typed 'docs'
    elif "docs" in websiteurl:
        texttospeech("Certainly, opening google docs now!")
        wb.open('https://docs.google.com/document/u/0/')

    #Creating ELIF statement to check if the user has typed 'email'
    elif "email" in websiteurl:
        texttospeech("Lets see if you received any emails, opening gmail now!")
        wb.open('https://mail.google.com/mail/u/0/#inbox')

    #Creating ELIF statement to check if the user has typed 'twitch'    
    elif "twitch" in websiteurl:
        texttospeech("Hope you find a good streamer to watch, opening twitch now!")
        wb.open('https://www.twitch.tv/')

    elif "facebook" in websiteurl:
        texttospeech("Opening facebook now!")
        wb.open('https://www.facebook.com/')
    else:
        texttospeech("I do not have that website programmed in me sir I can not open that website")
        