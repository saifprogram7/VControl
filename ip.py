import socket
from say import texttospeech

#Creating function to identify IP address
def ip():
    texttospeech("Sir this is sensitive information, I can not give this to you, please enter correct passcode")
    passcode1 = input("Please enter passcode: ")
    passcode2 = input("Please enter passcode: ")
    if passcode1 == "16" and passcode2 == "8":
            texttospeech("Access granted")
            hostname = socket.gethostname()
            ipaddress = socket.gethostbyname(hostname)
            texttospeech(ipaddress)
            print(ipaddress)    
    else:
        texttospeech("Potential Security Breach Detected!")