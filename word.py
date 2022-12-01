import os

#Creating variable to store word path
path = {
    'word' : "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\Word.lnk",
}

#Creating function to open word
def word():
    os.popen(path['word'])
