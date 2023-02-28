videoGames = ["Mario", "Sonic", "Joust", "Zelda"]

videoGames.append("Minecraft")
print(videoGames)

# the user asked to input a number between number 1 & 4, then the code checks weather it is a number within the videoGa
def pickGame():
    choice = int(input("Pick a Value Between 1 & "+ str(len(videoGames))))
    if (choice <= len(videoGames) and choice > 0):
        print(videoGames[choice - 1])
    else:
        pickGame()
pickGame()
gameChoice = input("Input a game that you like")

if(gameChoice in videoGames):
    videoGames.remove(gameChoice)
else:
    videoGames.append(gameChoice)
print(videoGames)