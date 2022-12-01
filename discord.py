import os

#Creating Path Variable
path = {
    'calculator': "C:\\Windows\\System32\\calc.exe"
}

#Creating function to open discord
def discord():
    os.startfile(path['discord'])
