### SETUP
import os
from WSDservices import services, thirdpartyservices
from os import system
system("title " + "WSD")
system("mode con:cols=50 lines=20")

### FUNCTION DECLARATIONS
    # DISABLE WINDOWS SERVICES

#| windows services start
def win_services():
    print("  ·   Enable / disable Windows services")
    print("  -   1 - Disable")
    print("  -   2 - Enable")
    userChoice = int(input(""))

    if userChoice == 1:
        for i in services:
            print("Trying to disable", i)
            os.system(f'cmd /c "sc config {i} start= disabled"')

    elif userChoice == 2:
        for i in services:
            print("Trying to enable", i)
            os.system(f'cmd /c "sc config {i} start= demand"')

#| windows services end
#| 3p services start
def thirdparty_services():
    print("  ·   Enable / disable Windows services")
    print("  -   1 - Disable")
    print("  -   2 - Enable")
    userChoice = int(input(""))

    if userChoice == 1:
        for i in thirdpartyservices:
            print("Trying to disable", i, "(3p)")
            os.system('cmd /c "sc config {} start= disabled"'.format(i))
    elif userChoice == 2:
        for i in thirdpartyservices:
            print("Trying to enable", i, "(3p)")
            os.system('cmd /c "sc config {} start= demand"'.format(i))

#| windows services end



### WELCOME SCREEN
print("")
print("           | Windows Service Debloater |")
print(" ")


### INIT USER CHOICE
print("  ·   Choose what you want to take an action on")
print("  -   1 - Windows services")
print("  -   2 - Third party services")

userChoice = int(input(""))
if userChoice == 1:
    win_services()
elif userChoice == 2:
    thirdparty_services()

print("Done!")
os.system("pause")
