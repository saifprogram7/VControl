import os

#Creating Path Variable
path = {
    'google chrome' : "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Google Chrome.lnk"
}


#Creating function to open google chrome
def chrome():
    os.startfile(path['google chrome'])