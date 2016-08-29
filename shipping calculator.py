def shipping_calculator(item_weight, num):

    while item_weight != float:
        print("Invalid option")
        if item_weight <= 5:
            cost = num * 5
        elif item_weight > 5 and item_weight <= 10:
            cost = num * 10
        elif item_weight > 10 and item_weight <= 20:
            cost = num * 15
        elif item_weight > 20:
            cost = num * 25
    return (cost)

def main():
    item_weight = float(input("please enter weight of item: "))
    num = input("Please enter the number of items: ")
    shipping_calculator(item_weight, num)
    if cost > 100:
        final_cost = cost *10 /100
    print("Fianl Cost is: $ ")
