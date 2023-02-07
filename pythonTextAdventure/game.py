import json
from colorama import Fore, Back, Style



with open("locations.json", "r") as read_file:
    data = json.load(read_file)

location = "001"

def main():
    newLocation = data[location]
    loadLocation(newLocation)
    optionSelection(newLocation["options"])

def loadLocation(location):
    print("-------------------------")
    print(Fore.RED + location["name"], Style.RESET_ALL)
    print(location["description"])
    print("Do you want to:")
    count = 0
    for item in location["options"]:
        count += 1
        print(str(count) + ". " + item["name"])

def optionSelection(options):
    choice = int(input(""))
    index = 0
    for option in options:
        index += 1
        if index == choice:
            global location
            location = option["rID"]

while True:
    main()