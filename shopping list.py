""" CP1404 Assignment 1 2016
    Shopping list 1.0

Pseudocode:
def get_menu_choice(choice)
    if choice.upper() is = to ["R"]:
        display required_items file
    elif choice.upper() is = ["C"]
        display completed_items file
def mark_item_completed()
    If choice is "M":
        display(required list of items)
        get number of item to be changed to completed, update csv file

Function main()
Display welcome message - by Dianne Sykes

def main()
    import csv file
    display contents of csv file
    display menu
    get choice from menu
    check input for errors

    if choice is "A":
        display ("what is to be added to shopping list")
        get new item to be added to shopping list
        get price and mark as required

    else:
       display ("number "items saved to item.csv
       Have a nice day :)
        """
def get_menu_choice(choice):
    if choice.upper() == ["R"]:
        return required_items.read(r)
    elif choice.upper()== ["C"]:
        return completed_items.read(c)
    elif choice.upper() == ["M"]:
        print(items.csv())








def main():
    shopping_list =[]

    # required_items = open("required_list.txt", "a")
    # item_list = required.read().strip()
    # required_items.close()
    # completed_items = open("completed.txt", "a")
    # item_list1 = completed.read().strip()
    # completed_items.close()

    import csv
    item_list_file = open("items.csv", "r")
    item_list_reader = csv.reader(item_list_file)
    for row in item_list_reader:
        print(row)

    print("Shopping list 1.0 - by Dianne Sykes")
    print("3 items loaded from items.csv")
    MENU = ["MENU:", "(R)List required items", "(C)List completed items", "(A)Add new Item", "(M) Mark an item as completed", "(Q) Quit"]
    for i in range(len(MENU)):
        print(MENU[i])
    choice = input().upper()
    while choice.upper() in ["R", "C", "M", "A"]:
        get_menu_choice()
    else:
        print("Invalid menu choice")
        choice = input().upper()





    else:
        print("{}" "items saved to items.csv".format(number_of_items))
        print("Have a nice day :)")


main()