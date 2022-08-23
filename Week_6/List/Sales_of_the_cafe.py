food_items = ["Cookies", "Donut", "Coke", "Sandwich", "Coffee"]     #initializing a list with food items 
items_price = [50, 50, 60, 100, 100]                              #initializing a list with the price of the items
items_supply = [10, 10, 10, 10, 10]                              #initializing a list with the supply of the items
sales = [0, 0, 0, 0, 0]                                          #initializing a sales list with values 0
max_transactions = 10                                            #assigning maximum transactions as 10

for sale in range(max_transactions):            #using for to get input from the customer
    print("Customer ", sale + 1)                #printing "Customer [number]"
    for item in range(len(food_items)):         #using for to iterate through the food items list
        print(food_items[item], " : Rs.", items_price[item])    #printing food items with price

    for item in range(len(food_items)):         #using for to iterate through the food items list
        no_of_item = int(input("How many " + str(food_items[item] + " do you want? : ")))   #reading input(order, in this case) from the customer
        if(no_of_item <= items_supply[item]):   #using if to check whether the ordered item has enough supply
            items_supply[item] -= no_of_item    #updating supply of item by subtracting the number of items ordered from the supply
            amount_earned = no_of_item * items_price[item]  #calculating amount earned by multiplying the number of items ordered with the price of the item
            sales[item] += amount_earned                #updating sales list by adding it with the amount earned
        elif(items_supply[item] == 0):            #using elif to check whether number of items added has no supply
            print("Out of stock.")                       #printing item is out of stock
        else:                                           #using else to see if the number of ordered item can be revised so that it is less than or equal to the supply
            print("Only ", items_supply[item], " of ", food_items[item], " is available")   #printing the quantity available for the orderd item
            print("Would like to revise your order? If yes press 1 else press 0")       #printing to ask if the customer would like to revise the order
            response = int(input())                             #reading response from the customer
            if(response == 1):                      #using if the customer's response is positive
                no_of_item = int(input("Out of " + str(items_supply[item]) + " How many " + str(food_items[item] + " do you want in : ")))                  #printing the available numbers of the item and asking how much does the customer want now
                if(no_of_item <= items_supply[item]):       #using if to check whether the ordered item has enough supply
                    items_supply[item] -= no_of_item        #updating supply of item by subtracting the number of items ordered from the supply
                    amount_earned = no_of_item * items_price[item]  #calculating amount earned by multiplying the number of items ordered with the price of the item
                    sales[item] += amount_earned            #updating sales list by adding it with the amount earned

for sale in range(len(sales)):                                 #using for to iterate through the sales list
    print("Sale in", food_items[sale], " - ", sales[sale])     #printing the food item with its corresponding sale



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