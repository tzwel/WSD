### SETUP
import os
from WSDservices import services, thirdpartyservices
from os import system
system("title " + "WSD")
system("mode con:cols=50 lines=20")

### FUNCTION DECLARATIONS
    # DISABLE WINDOWS SERVICES

def success():
    print("Done!")
    print("Press any key to exit.")
    os.system("pause >nul")

def exception():
    print("An exception has occurred.")
    print("WSD has been stopped. Press any key to exit.")
    os.system("pause >nul")

#| windows services start
def win_services():
    print("  ·   Enable / disable Windows services")
    print("  -   1 - Disable")
    print("  -   2 - Enable")
    userChoice = int(input(""))

    if userChoice == 1:
        try:
            for i in services:
                print("Trying to disable", i)
                os.system(f'cmd /c "sc config {i} start= disabled"')
        except:
            exception()
        else:
            success()

    elif userChoice == 2:
        try:
            for i in services:
                print("Trying to enable", i)
                os.system(f'cmd /c "sc config {i} start= demand"')
        except:
            exception()
        else:
            success()

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
            os.system(f'cmd /c "sc config {i} start= disabled"')
            success()

    elif userChoice == 2:
        for i in thirdpartyservices:
            print("Trying to enable", i, "(3p)")
            os.system(f'cmd /c "sc config {i} start= demand"')
            success()

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
