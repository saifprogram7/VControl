import os

#Creating Path Varaible to store path way
path = {
    'vs code' : "C:\\Users\\codew\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
}

#Creating function to open the vs code ide
def code():
    os.startfile(path['vs code'])