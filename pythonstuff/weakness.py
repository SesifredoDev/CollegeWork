
import random
weapons = ["water", "fire", "earth"]
zombieWeakness = weapons[random.randint(0, len(weapons)-1)]
print(zombieWeakness)

print("you have encountered a Zombie, prepare to fight. You have the following elements to fight with")
print(weapons)


def weaponChoices():
    addOrNot = int(input("if you want to use one of your existing ones, enter 2, if you want to add your own weapon press 1"))
    if addOrNot == 1:
        weapon = input("what weapon do you want to add?")
        weapons.append(weapon)
        weaponChoices()
    elif addOrNot == 2:
        weapon = input("Choose one of your weapons")
        if (weapon in weapons and weapon == zombieWeakness):
            print("you have sucessfully killed the zombie")
        else:
            print("keep trying trying, you can kill it")
            weaponChoices()
    else:
        weaponChoices()


weaponChoices()
