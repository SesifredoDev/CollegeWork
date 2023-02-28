from colorama import Fore, Back, Style
from side_by_side import print_side_by_side
import os

file_read = open("player.txt", "r")
pLines = file_read.readlines()
playerSprite = ""

for line in pLines:
    playerSprite += (line)

def fighting(player, monster, size):

    #MonsterSprite
    file_read = open("sprites/"+monster["sprite"], "r")
    mLines = file_read.readlines()

    monsterSprite = ""
    for line in mLines:
        monsterSprite += (line)


    while monster["hp"] > 0:
        #monster stats
        os.system('cls' if os.name == 'nt' else 'clear')
        
        print(Fore.RED + "-"*size + Style.RESET_ALL) #border

        monsterStats = ""
        monsterStats+= "You have run into: "+ Fore.RED + monster["monster"] + Style.RESET_ALL + "\n"
        monsterStats+= Fore.GREEN +"Health: "+ Style.RESET_ALL+ str(monster["hp"])

        print_side_by_side(monsterSprite, monsterStats)

        print(Fore.RED + "-"*size , Style.RESET_ALL) #border

        #player Stats
        weaponText = ""

        print("Here are your weapons")
        for i, weapon in enumerate(player["weapons"]):
            weaponText += (str(i)+ ". " + weapon["name"]+ " damage: " + Fore.BLUE + str(weapon["damage"]) + Style.RESET_ALL + "\n")

        print_side_by_side(playerSprite, weaponText)
        
        choice = input()



