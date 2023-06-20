import pyttsx3

#Jarvis voice output via speaker
speech = pyttsx3.init()
engine = speech.getProperty('voices')
speech.setProperty('voice', engine[1].id)
speech.setProperty('rate', 185)