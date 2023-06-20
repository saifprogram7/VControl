#Importing OS
import os

#Creating Path Variable
path = {
    'discord' : "C:\\Users\\codew\\OneDrive\\Desktop\\Desktop Folder\\Applications\\Discord.lnk"
}

#Creating function to open discord
def discord():
    os.startfile(path['discord'])
