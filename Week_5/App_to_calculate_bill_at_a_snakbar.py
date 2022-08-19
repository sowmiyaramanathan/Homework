coffee_price = 100      #initializing coffee price
vadai_price = 100       #initializing vadai price
sandwich_price = 200    #initializing sandwich price
coke_price = 60         #initializing coke price
total_price = 0         #initialiaing total price as 0

total_coffee = int(input("Enter the number of coffee the customer bought: "))
total_vadai = int(input("Enter the number of vadais the customer bought: "))
total_sandwich = int(input("Enter the number of sandwich the customer bought: "))
total_coke = int(input("Enter the number of coke the customer bought: "))

coffee_price *= total_coffee
vadai_price *= total_vadai
sandwich_price *= total_sandwich
coke_price *= total_coke
total_price =  coffee_price + vadai_price + sandwich_price + coke_price

if(total_coffee>=1 and total_vadai>=1 and total_sandwich>=1 or total_coke>=1):
    discount = 20
    total_price = total_price - (total_price * discount / 100)
elif(total_price>1000):
    discount = 20
    total_price = total_price - (total_price * discount / 100)
elif(total_sandwich > 1 or total_vadai > 2):
    total_price -= coffee_price
    price_of_coffee = 50
    coffee_price = total_coffee * price_of_coffee
    total_price += coffee_price

print("Total cost of items : ", total_price)