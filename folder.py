import os
from say import texttospeech

#Creating Variable to store File Path
directory = {
    'desktop' : "C:\\Users\\codew\\OneDrive\\Desktop",
    'university project' : "C:\\Users\\codew\\OneDrive\\Desktop\\University Project", 
    'documentation' : "C:\\Users\\codew\\OneDrive\\Desktop\\University Project\\Documentation",
    'code' : "C:\\Users\\codew\\OneDrive\\Desktop\\University Project\\Code"
}

#Creating Function to check folder exsists
def folder_check(build):
    if not os.path.exists(build):
        os.makedirs(build, mode = 0o777)
        texttospeech("I have successfully created the folder!")
    else:
        texttospeech("This folder already exsists")
        texttospeech("Please try again")
        folder()

#Creating Function to build a folder
def folder():
    texttospeech("what location would you like the folder?")
    location = input("What location would you like the folder: ")
    
    #IF statement for desktop
    if "desktop" in location:
        texttospeech("Certainly, what name should I give to the folder?")
        name = input("What name should I give to the folder: ")
        texttospeech("Abosolutely sir, creating folder now!")
        build = os.path.join(directory['desktop'], name)
        
        #Calling folder check
        folder_check(build)

    #ELIF statement for university project
    elif "university project" in location:
        texttospeech("Certainly, what name should I give to the folder?")
        name = input("What name should I give to the folder: ")
        texttospeech("Abosolutely sir, creating folder now!")
        build = os.path.join(directory['university project'], name)
        
        #Calling folder check
        folder_check(build)
    
    #ELIF statement for documentation
    elif "documentation" in location:
        texttospeech("Certainly, what name should I give to the folder?")
        name = input("What name should I give to the folder: ")
        texttospeech("Abosolutely sir, creating folder now!")
        build = os.path.join(directory['documentation'], name)
        
        #Calling folder check
        folder_check(build)

    #ELIF statement for code
    elif "code" in location:
        texttospeech("Certainly, what name should I give to the folder?")
        name = input("What name should I give to the folder: ")
        texttospeech("Abosolutely sir, creating folder now!")
        build = os.path.join(directory['code'], name)
        
        #Calling folder check
        folder_check(build)
