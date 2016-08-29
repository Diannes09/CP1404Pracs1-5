import random

MAX_INCREASE = 0.1  # 10%
MAX_DECREASE = 0.1  # 5%
MIN_PRICE = 0.01
MAX_PRICE = 1000.0
INITIAL_PRICE = 10.0
price = INITIAL_PRICE
day = 1

#print("${:,.2f}".format(price))
print("Starting price:${:,.2f}".format(price))
while price >= MIN_PRICE and price <= MAX_PRICE:
    price_change = 0
    # generate a random integer of 1 or 2
    # if it's 1, the price increases, otherwise it decreases
    if random.randint(1, 2) == 1:
        # generate a random floating-point number
        # between 0 and MAX_INCREASE
        price_change = random.uniform(0, MAX_INCREASE)
    else:
        # generate a random floating-point number
        # between negative MAX_INCREASE and 0
        price_change = random.uniform(-MAX_DECREASE, 0)

    price *= (1 + price_change)
    number = int(price)

    print("On day {} price is: ${:,.2f}".format(day,price))
    day += 1


