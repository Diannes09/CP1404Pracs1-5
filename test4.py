finished = False
result = 0
while not finished:
    try:
        number = int(input("please enter a numer:"))# TODO: this line
        result = (10/number) # TODO: this line
        finished = True
    except ZeroDivisionError:
        print("Cant divide by zero.")
    except ValueError:  # TODO - add something after except
        print("Please enter a valid integer.")
print("Valid result is:", result)