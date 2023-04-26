import clipboard
import sys
import json
import colorama
from colorama import Fore, Back, Style
import os

colorama.init(autoreset=True)

COMMANDs = ["save", "load", "list", "delete"] 
FILEPATH = "myData.json"
ENTRY_PASS = 100110


def save_data(filePath, data):
    with open(file=filePath, mode="w") as f:
        json.dump(data, f)


def load_data(filePath):
    try:
        with open(file=filePath, mode="r") as f:
            DATA = json.load(f)
            return DATA
    except:
        pass


if len(sys.argv) == 2:
    USER_COMMAND = sys.argv[1]
    DATA = load_data(filePath=FILEPATH)

    if USER_COMMAND == COMMANDs[0]:
        print(Fore.MAGENTA + Style.BRIGHT + "Enter a key: ")
        KEY = input()
        if DATA is not None:
            DATA[KEY] = clipboard.paste()
        else:
            DATA = {KEY: clipboard.paste()}
        save_data(filePath=FILEPATH, data=DATA)
        print(Fore.GREEN + Style.BRIGHT + "[SAVED] data saved")

    elif USER_COMMAND == COMMANDs[1]:
        print(Fore.MAGENTA + Style.BRIGHT + "Enter a key: ")
        KEY = input()
        if DATA is not None:
            if clipboard.paste() != DATA[KEY]:
                clipboard.copy(DATA[KEY])
                print(Fore.CYAN + Style.BRIGHT + "[COPIED] data copied to clipboard")
            else:
                print(Fore.YELLOW + Style.BRIGHT + "already on clipboard")
        else:
            print(Fore.BLACK + Style.BRIGHT + Back.RED + "(!) No such key exists.")

    elif USER_COMMAND == COMMANDs[2]:
        if DATA is not None:
            print(Fore.MAGENTA + Style.BRIGHT + "Enter Code(6-digit): ")
            CODE = input()
            if int(CODE) == ENTRY_PASS:
                print(DATA)
            else:
                print(type(CODE), type(ENTRY_PASS))
        else:
            print(Fore.YELLOW + Style.BRIGHT + "Nothing to show | add data using save command")

    elif USER_COMMAND == COMMANDs[3]:
        if DATA is not None:
            print(Fore.RED + "do you want to delete? (y/n): ")
            VAL = input()
            if VAL.lower() == "y":
                os.unlink(FILEPATH)
                print(Fore.CYAN + "[DELETED] file deleted")
        else:
            print(Fore.YELLOW + Style.BRIGHT + "No file exists")

    else:
        print(Fore.RED + Style.BRIGHT + "Unknown command.")
        print("Commands: ", COMMANDs)

else:
    print(Fore.RED + Style.BRIGHT + "[ERROR] takes exactly one command")
    print("Commands: ", COMMANDs)
