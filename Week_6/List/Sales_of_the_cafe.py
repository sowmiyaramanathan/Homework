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
    print("Do you want to continue? Yes/No : ")
    response = input()
    if(response == "No"):
        break
for sale in range(len(sales)):                                 #using for to iterate through the sales list
    print("Sale in", food_items[sale], " - ", sales[sale])     #printing the food item with its corresponding sale



"""
test case 1
Cookies  : Rs. 50
Donut  : Rs. 50
Coke  : Rs. 60
Sandwich  : Rs. 100
Coffee  : Rs. 100
How many Cookies do you want? : 2
How many Donut do you want? : 0
How many Coke do you want? : 2
How many Sandwich do you want? : 3
How many Coffee do you want? : 1
Do you want to continue? Yes/No : 
Yes
Customer  2
Cookies  : Rs. 50
Donut  : Rs. 50
Coke  : Rs. 60
Sandwich  : Rs. 100
Coffee  : Rs. 100
How many Cookies do you want? : 3
How many Donut do you want? : 5
How many Coke do you want? : 2
How many Sandwich do you want? : 4
How many Coffee do you want? : 2
Do you want to continue? Yes/No : 
Yes
Customer  3
Cookies  : Rs. 50
Donut  : Rs. 50
Coke  : Rs. 60
Sandwich  : Rs. 100
Coffee  : Rs. 100
How many Cookies do you want? : 4
How many Donut do you want? : 2
How many Coke do you want? : 2
How many Sandwich do you want? : 3
How many Coffee do you want? : 1
Do you want to continue? Yes/No : 
Yes
Customer  4
Cookies  : Rs. 50
Donut  : Rs. 50
Coke  : Rs. 60
Sandwich  : Rs. 100
Coffee  : Rs. 100
How many Cookies do you want? : 0
How many Donut do you want? : 3
How many Coke do you want? : 2
How many Sandwich do you want? : 1
Out of stock.
How many Coffee do you want? : 1
Do you want to continue? Yes/No : 
No
Sale in Cookies  -  450
Sale in Donut  -  500
Sale in Coke  -  480
Sale in Sandwich  -  1000
Sale in Coffee  -  500
"""