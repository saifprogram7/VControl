from voice import speech

#Jarvis Speech Function
def texttospeech(text_to_say):
    speech.say(text_to_say)
    speech.runAndWait()