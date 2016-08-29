def main():
    item_cost = float(input("Enter item price: "))
    num = int(input("Enter number of items: "))
    while num <= 0:
        print("Invalid number of items! Please retry")
        num = int(input("Enter number of items: "))
    final_cost = item_cost * num
    if final_cost > 100:
        discount = final_cost *10 /100
        final_cost = final_cost - discount
    print("Fianl Cost is: $ " + str(final_cost))

main()