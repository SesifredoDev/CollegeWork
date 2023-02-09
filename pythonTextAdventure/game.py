import json
from colorama import Fore, Back, Style
import os

size = os.get_terminal_size().columns*2
print(size)

with open("locations.json", "r") as read_file:
    data = json.load(read_file)

location = 0

def main():
    newLocation = data[location]
    loadLocation(newLocation)
    choice = int(input(""))
    optionSelection(newLocation["options"], choice)

def loadLocation(location):
    print(Fore.BLUE + "-"*size , Style.RESET_ALL)
    print(Fore.RED + location["name"], Style.RESET_ALL)
    print(location["description"])
    print("Do you want to:")
    count = 0
    for item in location["options"]:
        count += 1
        print(str(count) + ". " + item["name"])

def optionSelection(options, choice):
    if (choice <= len(options)):
        global location 
        location = options[choice - 1]["rID"]
    else:
        choice = int(input("Select an option above: \n"))
        optionSelection(options, choice)
while True:
    main()