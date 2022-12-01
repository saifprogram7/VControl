import subprocess as sp

#Creating Path Variable
path = {
    'calculator': "C:\\Windows\\System32\\calc.exe"
}

#Creating function to open the calculator
def calculator():
    sp.Popen(path['calculator'])