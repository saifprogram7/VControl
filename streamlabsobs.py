import os

#Creating variable to store obs path
path = {
    'streamlabs' : "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Streamlabs Desktop.lnk",
}

#Creating function to open obs
def streamlabsOBS():
    os.popen(path['streamlabs'])
