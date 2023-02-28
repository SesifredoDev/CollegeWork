names = ["Mario", "Sonic", "Dude", "Zelda"]
print(names)
# the user asked to input a number between number 1 & 4, then the code checks weather it is a number within the names
name = input("Input your Name")
location = int(input("Pick a number between 0 & " + str(len(names)-1)))

names.pop(location)
names.insert(location, name)

print(names)