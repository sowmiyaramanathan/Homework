coffee_price = 100      #initializing coffee price
vadai_price = 100       #initializing vadai price
sandwich_price = 200    #initializing sandwich price
coke_price = 60         #initializing coke price
total_price = 0         #initializing total price as 0

print("Coffee - Rs.100 \nVadai - Rs. 100 \nSandwich - Rs.200 \nCoke - Rs.60") #printing available items with their price
total_coffee = int(input("Enter the number of coffee the customer bought: "))   #reading the number of coffee the customer bought
total_vadai = int(input("Enter the number of vadais the customer bought: "))    #reading the number of vadai the customer bought
total_sandwich = int(input("Enter the number of sandwich the customer bought: "))   #reading the number of sandwich the customer bought
total_coke = int(input("Enter the number of coke the customer bought: "))   #reading the number of coke the customer bought

coffee_price *= total_coffee    #calculating price of coffee by multiplying number of coffee with price
vadai_price *= total_vadai      #calculating price of vadai by multiplying number of vadai with price
sandwich_price *= total_sandwich    #calculating price of sandwich by multiplying number of sandwich with price
coke_price *= total_coke        #calculating price of coke by multiplying number of coke with price
total_price =  coffee_price + vadai_price + sandwich_price + coke_price     #calculating total price of items by adding the price of each items

if(total_coffee >= 1 and total_vadai >= 1 and total_sandwich >= 1 and total_coke >= 1):  #using if to check if the customer has bought atleast one or more number of items in each
    discount = 20       #initializing a discount of 20
    total_price = total_price - (total_price * discount / 100)  #applying the discount on the total price
elif(total_price > 1000):     #using if to check if the total price is greater than 1000
    discount = 20       #initializing a discount of 20
    total_price = total_price - (total_price * discount / 100)  #applying the discount on the total price
elif(total_coffee >= 1):        #using if to check if total coffee is greater than 1 to see if we can apply discount
    if(total_sandwich > 1 or total_vadai > 2):  #using if to check if sandwich is more than 1 or total vadai is greater than 2
        total_price -= coffee_price                     #subtracting the actual coffee price from the total price to apply discount and then calculate the total price
        price_of_one_coffee = 50                            #initializing the price of as 50
        coffee_price = total_coffee * price_of_one_coffee   #calculating coffee price by multiplying the number of coffee with the new price for each coffee the customer bought
        total_price += coffee_price         #calculating the total price by adding the total price with the coffee price

print("Total cost of items : Rs.", total_price)            #printing the total cost



#discount for buying all items atleast once
#Coffee - Rs.100 
#Vadai - Rs. 100
#Sandwich - Rs.200
#Coke - Rs.60
#Enter the number of coffee the customer bought: 4
#Enter the number of vadais the customer bought: 2
#Enter the number of sandwich the customer bought: 2
#Enter the number of coke the customer bought: 3
#Total cost of items : Rs. 944.0

#no discount
#Coffee - Rs.100 
#Vadai - Rs. 100
#Sandwich - Rs.200
#Coke - Rs.60
#Enter the number of coffee the customer bought: 0
#Enter the number of vadais the customer bought: 0
#Enter the number of sandwich the customer bought: 3 
#Enter the number of coke the customer bought: 1
#Total cost of items : Rs. 660

#discount for above Rs.1000
#Coffee - Rs.100 
#Vadai - Rs. 100
#Sandwich - Rs.200
#Coke - Rs.60
#Enter the number of coffee the customer bought: 5
#Enter the number of vadais the customer bought: 7
#Enter the number of sandwich the customer bought: 0
#Enter the number of coke the customer bought: 1
#Total cost of items : Rs. 1008.0

#discount for coffee
#Coffee - Rs.100 
#Vadai - Rs. 100
#Sandwich - Rs.200
#Coke - Rs.60
#Enter the number of coffee the customer bought: 2
#Enter the number of vadais the customer bought: 3
#Enter the number of sandwich the customer bought: 0
#Enter the number of coke the customer bought: 0
#Total cost of items : Rs. 400
