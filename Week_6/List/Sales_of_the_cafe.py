food_items = ["Cookies", "Donut", "Coke", "Sandwich", "Coffee"]
items_price = [50, 50, 60, 100, 100]
items_supply = [10, 10, 10, 10, 10]
sales = [0, 0, 0, 0, 0]
max_transactions = 10

for sale in range(max_transactions):
    print("Customer ", sale + 1)
    for item in range(len(food_items)):
        print(food_items[item], " : Rs.", items_price[item])

    for item in range(len(food_items)):
        no_of_item = int(input("How many " + str(food_items[item] + " do you want? : ")))
        if(no_of_item <= items_supply[item]):
            items_supply[item] -= no_of_item
            amount_earned = no_of_item * items_price[item]
            sales[item] += amount_earned
        elif(items_supply[item] == 0):
            print("Out of stock.")
        else:
            print("Only ", items_supply[item], " of ", food_items[item], " is available")
            print("Would like to revise your order? If yes press 1 else press 0")
            response = int(input())
            if(response == 1):
                no_of_item = int(input("Out of " + str(items_supply[item]) + " How many " + str(food_items[item] + " do you want in : ")))
                if(no_of_item <= items_supply[item]):
                    items_supply[item] -= no_of_item
                    amount_earned = no_of_item * items_price[item]
                    sales[item] += amount_earned

for sale in range(len(sales)):
    print("Sale in", food_items[sale], " - ", sales[sale])



# test case 1
# Cookies  : Rs. 50
# Donut  : Rs. 50
# Coke  : Rs. 60
# Sandwich  : Rs. 100
# Coffee  : Rs. 100
# Customer  1
# How many Cookies do you want? : 20
# How many Donut do you want? : 0
# How many Coke do you want? : 5
# How many Sandwich do you want? : 2
# How many Coffee do you want? : 2
# Customer  2
# How many Cookies do you want? : 50
# How many Donut do you want? : 10
# How many Coke do you want? : 10
# How many Sandwich do you want? : 30
# How many Coffee do you want? : 80 
# Customer  3
# How many Cookies do you want? : 8
# How many Donut do you want? : 4
# How many Coke do you want? : 3
# How many Sandwich do you want? : 5
# How many Coffee do you want? : 4
# Customer  4
# How many Cookies do you want? : 90
# How many Donut do you want? : 30
# How many Coke do you want? : 50
# How many Sandwich do you want? : 20
# How many Coffee do you want? : 10
# Customer  5
# How many Cookies do you want? : 20
# How many Donut do you want? : 5
# How many Coke do you want? : 10
# How many Sandwich do you want? : 5
# Out of stock
# How many Coffee do you want? : 8
# Out of stock
# Customer  6
# How many Cookies do you want? : 40
# Out of stock
# How many Donut do you want? : 5
# Out of stock
# How many Coke do you want? : 7
# How many Sandwich do you want? : 8
# Out of stock
# How many Coffee do you want? : 6
# Out of stock
# Customer  7
# How many Cookies do you want? : 8
# How many Donut do you want? : 4
# Out of stock
# How many Coke do you want? : 5
# How many Sandwich do you want? : 3
# How many Coffee do you want? : 5
# Out of stock
# Customer  8
# How many Cookies do you want? : 7
# Out of stock
# How many Donut do you want? : 8
# Out of stock
# How many Coke do you want? : 5
# How many Sandwich do you want? : 5
# Out of stock
# How many Coffee do you want? : 2
# Customer  9
# How many Cookies do you want? : 2
# How many Donut do you want? : 3
# Out of stock
# How many Coke do you want? : 4
# How many Sandwich do you want? : 7
# Out of stock
# How many Coffee do you want? : 2
# Customer  10
# How many Cookies do you want? : 2
# How many Donut do you want? : 1
# How many Coke do you want? : 4
# Out of stock
# How many Sandwich do you want? : 2
# Out of stock
# How many Coffee do you want? : 1
# Out of stock
# Sale in  Cookies  -  10000
# Sale in  Donut  -  2500
# Sale in  Coke  -  5940
# Sale in  Sandwich  -  6000
# Sale in  Coffee  -  10000

# test case 2
# Customer  1
# Cookies  : Rs. 50
# Donut  : Rs. 50
# Coke  : Rs. 60
# Sandwich  : Rs. 100
# Coffee  : Rs. 100
# How many Cookies do you want? : 2
# How many Donut do you want? : 2
# How many Coke do you want? : 2
# How many Sandwich do you want? : 2
# How many Coffee do you want? : 2
# Customer  2
# Cookies  : Rs. 50
# Donut  : Rs. 50
# Coke  : Rs. 60
# Sandwich  : Rs. 100
# Coffee  : Rs. 100
# How many Cookies do you want? : 3
# How many Donut do you want? : 0
# How many Coke do you want? : 0
# How many Sandwich do you want? : 3
# How many Coffee do you want? : 1
# Customer  3
# Cookies  : Rs. 50
# Donut  : Rs. 50
# Coke  : Rs. 60
# Sandwich  : Rs. 100
# Coffee  : Rs. 100
# How many Cookies do you want? : 5
# How many Donut do you want? : 2
# How many Coke do you want? : 2
# How many Sandwich do you want? : 3
# How many Coffee do you want? : 2
# Customer  4
# Cookies  : Rs. 50
# Donut  : Rs. 50
# Coke  : Rs. 60
# Sandwich  : Rs. 100
# Coffee  : Rs. 100
# How many Cookies do you want? : 2
# Out of stock.
# How many Donut do you want? : 2
# How many Coke do you want? : 2
# How many Sandwich do you want? : 2
# How many Coffee do you want? : 1
# Customer  5
# Cookies  : Rs. 50
# Donut  : Rs. 50
# Coke  : Rs. 60
# Sandwich  : Rs. 100
# Coffee  : Rs. 100
# How many Cookies do you want? : 2
# Out of stock.
# How many Donut do you want? : 2
# How many Coke do you want? : 2
# How many Sandwich do you want? : 2
# Out of stock.
# How many Coffee do you want? : 1
# Customer  6
# Cookies  : Rs. 50
# Donut  : Rs. 50
# Coke  : Rs. 60
# Sandwich  : Rs. 100
# Coffee  : Rs. 100
# How many Cookies do you want? : 1
# Out of stock.
# How many Donut do you want? : 1
# How many Coke do you want? : 1
# How many Sandwich do you want? : 1
# Out of stock.
# How many Coffee do you want? : 1
# Customer  7
# Cookies  : Rs. 50
# Donut  : Rs. 50
# Coke  : Rs. 60
# Sandwich  : Rs. 100
# Coffee  : Rs. 100
# How many Cookies do you want? : 2
# Out of stock.
# How many Donut do you want? : 2
# Only  1  of  Donut  is available
# Would like to revise your order? If yes press 1 else press 0
# 1
# Out of 1 How many Donut do you want in : 1
# How many Coke do you want? : 3
# Only  1  of  Coke  is available
# Would like to revise your order? If yes press 1 else press 0
# 1
# Out of 1 How many Coke do you want in : 1
# How many Sandwich do you want? : 1
# Out of stock.
# How many Coffee do you want? : 2
# Customer  8
# Cookies  : Rs. 50
# Donut  : Rs. 50
# Coke  : Rs. 60
# Sandwich  : Rs. 100
# Coffee  : Rs. 100
# How many Cookies do you want? : 1
# Out of stock.
# How many Donut do you want? : 1
# Out of stock.
# How many Coke do you want? : 1
# Out of stock.
# How many Sandwich do you want? : 1
# Out of stock.
# How many Coffee do you want? : 1
# Out of stock.
# Customer  9
# Cookies  : Rs. 50
# Donut  : Rs. 50
# Coke  : Rs. 60
# Sandwich  : Rs. 100
# Coffee  : Rs. 100
# How many Cookies do you want? : 5
# Out of stock.
# How many Donut do you want? : 54
# Out of stock.
# How many Coke do you want? : 5
# Out of stock.
# How many Sandwich do you want? : 52
# Out of stock.
# How many Coffee do you want? : 2
# Out of stock.
# Customer  10
# Cookies  : Rs. 50
# Donut  : Rs. 50
# Coke  : Rs. 60
# Sandwich  : Rs. 100
# Coffee  : Rs. 100
# How many Cookies do you want? : 2
# Out of stock.
# How many Donut do you want? : 2
# Out of stock.
# How many Coke do you want? : 2
# Out of stock.
# How many Sandwich do you want? : 2
# Out of stock.
# How many Coffee do you want? : 2
# Out of stock.
# Sale in Cookies  -  500
# Sale in Donut  -  500
# Sale in Coke  -  600
# Sale in Sandwich  -  1000
# Sale in Coffee  -  1000