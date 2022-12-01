import os

#Creating variable to store powerpoint path
path = {
    'powerpoint' : "C:\ProgramData\Microsoft\Windows\Start Menu\Programs\PowerPoint.lnk"
}

#Creating function to open powerpoint
def powerpoint():
    os.popen(path['powerpoint'])
