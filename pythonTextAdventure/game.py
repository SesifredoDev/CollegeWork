import json
import random
from colorama import Fore, Back, Style
import os
import pygame
from filter import *
from combat import *


size = os.get_terminal_size().columns*2
print(size)

with open("locations.json", "r") as read_file:
    data = json.load(read_file)

location = 0
encounterList = data["encounters"]
player = data["player"]
def main():
    newLocation = data["story"][location]
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
        if (options[choice - 1]["encounter"] != False):
            loadEncounter(options[choice - 1]["encounter"])
        else:
            pass
    else:
        choice = int(input("Select an option above: \n"))
        optionSelection(options, choice)

def loadEncounter(level):
    monstersFiltered = filterNumFunc(encounterList, "level", level)
    monsterChoice = random.randint(0, len(monstersFiltered)-1)
    monster = monstersFiltered[monsterChoice]
    fighting(player, monster, size)
    

while True:
    os.system('cls' if os.name == 'nt' else 'clear')
    main()
    