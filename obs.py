import os

#Creating variable to store obs path
path = {
    'obs' : "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\OBS Studio\\OBS Studio (64bit).lnk",
}

#Creating function to open obs
def obs():
    os.popen(path['obs'])
