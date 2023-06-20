from say import texttospeech

def standby():
    texttospeech("Going on stand by mode")
    prompt = input("> ")
    if "wake up" in prompt:
        texttospeech("I am now back online")