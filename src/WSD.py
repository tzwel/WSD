### SETUP
import os
from os import system
system("title " + "WSD")

services = [
    "uhssvc",         # Microsoft Update Health Service
    "wuauserv",       # Windows Update Service
    "XboxGipSvc",     # Xbox Accessory Management Service
    "XblGameSave",    # Xbox Live Game Save Service
    "XblAuthManager", # Xbox Live Auth Manager
    "XboxNetApiSvc",  # Xbox Live Networking Service
    "wercplsupport",  # Problem Reports and Solutions
    "WalletService",  # Wallet Service
    "Fax",            # Fax
    "WerSvc",         # Windows Error Reporting Service
    "pla",            # Performance logs and alerts
    "RstMwService",   # Intel® Rapid Storage Technology Management Service
    "lfsvc",          # Geolocation Service
    "diagnosticshub.standardcollector.service",
                      # Microsoft® Diagnostics Hub Standard Collector
    "wlidsvc",        # Microsoft Windows Live ID Service
    "PNRPAutoReg",    # PNRP Machine Name Publication Service
    "WMPNetworkSvc",  # Windows Media Player Network Sharing Service
    "icssvc",         # Windows Mobile Hotspot Service
    "DoSvc"           # Delivery Optimization service
]

### FUNCTION DECLARATIONS
def disable_services():
    for i in services:
        print("Trying to disable", i)
        os.system('cmd /c "sc config {} start= disabled"'.format(i))

def enable_services():
    for i in services:
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
