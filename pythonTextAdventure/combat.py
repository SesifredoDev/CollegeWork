from colorama import Fore, Back, Style
from side_by_side import print_side_by_side
import random
import os





def fighting(player, monster, size):
    combat = True
    #MonsterSprite
    file_read = open("sprites/"+monster["sprite"], "r")
    mLines = file_read.readlines()

    monsterSprite = ""
    for line in mLines:
        monsterSprite += (line)

    #player sprite
    file_read = open("sprites/player.txt", "r")
    pLines = file_read.readlines()
    playerSprite = ""

    for line in pLines:
        playerSprite += (line)


    while combat == True:

        #monster stats
        os.system('cls' if os.name == 'nt' else 'clear')
        
        print(Fore.RED + "-"*size + Style.RESET_ALL) #border

        monsterStats = ""
        monsterStats+= "You have run into: "+ Fore.RED + monster["monster"] + Style.RESET_ALL + "\n"
        monsterStats+= Fore.GREEN +"Health: "+ Style.RESET_ALL+ str(monster["hp"])

        print_side_by_side(monsterSprite, monsterStats)

        print(Fore.RED + "-"*size , Style.RESET_ALL) #border

        #player Stats
        playerStats = ""
        weaponText = "Here are your weapons \n"

        

        for i, weapon in enumerate(player["weapons"]):
            weaponText += (str(i)+ ". " + weapon["name"]+ " damage: " + Fore.BLUE + str(weapon["damage"]) + Style.RESET_ALL + "\n")

        playerStats += Fore.GREEN +"Health: "+ Style.RESET_ALL+ str(player["hp"]) + "\n \n"
        playerStats += weaponText

        print_side_by_side(playerSprite, playerStats)


        #choose an Attack
        chooseAttack(player, monster)
        if(player["hp"] <= 0):
            print("Game Over, Start Over? press Enter")
            enter = input()
            player["hp"] = player["maxHp"]
            monster["hp"] = monster["maxHp"]
            combat = False
            location = 0
        elif(monster["hp"] <= 0):
            print("Congrats! move foward?")
            enter = input()
            player["hp"] = player["maxHp"]
            monster["hp"] = monster["maxHp"]
            combat = False
        else:
            pass
        

    


def chooseAttack(player, monster):          
    choice = int(input())
    if(choice >= 0 and choice < len(player["weapons"])):
        monster["hp"] -= player["weapons"][choice]["damage"]
        player["hp"] -= int(random.randint(monster["damage"]["min"], monster["damage"]["max"]))
    else:
        chooseAttack(player, monster)