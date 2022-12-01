import os
from say import texttospeech

#Creating Variable to store File Path
directory = {
    'desktop' : "C:\\Users\\codew\\OneDrive\\Desktop",
    'university project' : "C:\\Users\\codew\\OneDrive\\Desktop\\University Project", 
    'documentation' : "C:\\Users\\codew\\OneDrive\\Desktop\\University Project\\Documentation",
    'code' : "C:\\Users\\codew\\OneDrive\\Desktop\\University Project\\Code"
}

#Creating function to make a file
def file():
    texttospeech("What is the file name with file extension?")
    buildingfile = input("What is the file name with extension: ").lower()
    texttospeech("Where would you like me to create this file?")
    filelocation = input("Where would you like me to create this file: ").lower()
    if "desktop" in filelocation:
        filebuild = directory['desktop']+"/"+buildingfile
        texttospeech("That is all done for you now!")
        open(filebuild, 'a').close()
    elif "university project" in filelocation:
        filebuild = directory['university project']+"/"+buildingfile
        texttospeech("That is all done for you now!")
        open(filebuild, 'a').close()
    elif "documentation" in filelocation:
        filebuild = directory['documentation']+"/"+buildingfile
        texttospeech("That is all done for you now!")
        open(filebuild, 'a').close()
    elif "code" in filelocation:
        filebuild = directory['code']+"/"+buildingfile
        texttospeech("That is all done for you now!")
        open(filebuild, 'a').close()