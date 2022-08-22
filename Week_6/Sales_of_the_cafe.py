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