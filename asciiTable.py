def main():
    lower = 10
    upper = 100
    number = int(input("Enter a number {} - {},\n >>> ".format(lower, upper)))
    while not 10 < number < 100:
        print("please enter a valid number")
        number = int(input("Enter a number {} - {},\n >>> ".format(lower, upper)))
        print(number)


main()

