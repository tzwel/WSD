### SETUP
import os
from os import system
system("title " + "WSD")

disable = [
    "uhssvc",
    "wuauserv",
    "XboxGipSvc",
    "XblGameSave",
    "wercplsupport",
    "WalletService",
    "Fax",
    "WerSvc"
]

### FUNCTION DECLARATIONS
def disable_services():
    for i in disable:
        print("Trying to disable", i)
        os.system('cmd /c "sc config {} start= disabled"'.format(i))

def enable_services():
    for i in disable:
        print("Trying to enable", i)
        os.system('cmd /c "sc config {} start= demand"'.format(i))

### WELCOME SCREEN
print(" / ============================================== \ ")
print("|             Windows Service Debloater            |")
print(" \ ============================================== / ")


### USER CHOICE
print("  |   Type:")
print("  |   1 - To disable unnecessary services")
print("  |   2 - To enable unnecessary services")

userChoice = int(input(""))
if userChoice == 1:
    disable_services()
elif userChoice == 2:
    enable_services()

os.system("pause")
