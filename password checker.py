MIN_LENGTH = 2
MAX_LENGTH = 6
SPECIAL_CHARS_REQUIRED = False
SPECIALS = "!@#$%^&*()_-=+`~,./'[]\<>?{}|"


def main():
    print("Please enter a valid password")
    print("Your password must be between", MIN_LENGTH, "and", MAX_LENGTH, "characters, and contain:")
    print("\t1 or more uppercase characters")
    print("\t1 or more lowercase characters")
    print("\t1 or more numbers")
    if SPECIAL_CHARS_REQUIRED:
        print("\tand 1 or more special characters: ", SPECIALS)
    password = input("> ")
    while not is_valid_password(password):
        print("Invalid password!")
        password = input("> ")
    print("Your " + str(len(password)) + " character password is valid: " + password)


def is_valid_password(password):
    #check_password = open("check.txt", "r")
    #password = check_password.read().strip()
    for char in password:
        if 6 < len(password) > 2:# TODO: if length is wrong, return False
          return True
        else:
            count_lower = 0
            count_upper = 0
            count_digit = 0
            count_special = 0
            for char in password:
                if char.isdigit():
                    count_digit += 1
                if char.islower():
                    count_lower += 1
                if char.isupper():
                    count_upper += 1
                #if char.isspecial():
                    #count_special += 1 # TODO: count each kind of character

                for i in password:
                    if count_digit != 0 and count_lower != 0 and count_upper != 0: #and count_special !=0:
                        return True





main()