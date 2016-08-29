newOne = open("name.txt", "r")
name = newOne.read().strip()
print("Your name is:", name)
newOne.close()