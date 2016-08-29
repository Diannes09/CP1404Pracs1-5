def main():
    newFile = open("name.txt", "w")
    name = input("What is your name?")
    print(name, file= newFile)
    newFile.close()

main()
