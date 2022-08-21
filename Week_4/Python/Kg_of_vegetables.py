onion_price = 20.0      #price of onion is 20.0
tomato_price = 10.5     #price of tomato is 10.5
budget = float(input("Enter your budget : "))       #reading budget from the customer to know how many kg of vegetables the customer can buy with that amount
kg_of_onions = 0        #initializing total kg of onions to 0
kg_of_tomatoes = 0      #initializing total kg of tomatoes to 0

if(budget == 0):        #using if to check whether the budget if 0
    print("You cannot buy vegetables")      #printing that customer cannot buy any vegetables

else:
    while(onion_price <= budget):     #using while loop to calculate the price of onion when increasing its quantity by 1kg
        onion_price += 20.0     #increasing the price of onions by the price amount for 1 kg
        kg_of_onions += 1       #increasing the quantity of onions 1kg at a time

    while(tomato_price <= budget):      #using while loop to calculate the price of tomato when increasing its quantity by 1kg
        tomato_price += 10.5        #increasing the price of tomatoes by the price amount for 1 kg
        kg_of_tomatoes += 1     #increasing the quantity of tomatoes 1kg at a time

    print("Total kg of onions you can buy within your budget: ", kg_of_onions, "kg")        #printing the total kg of onion the customer can buy with the budget amount
    print("or")                                                                             #printing otherwise
    print("Total kg of tomatoes you can buy within your budget: ", kg_of_tomatoes, "kg")    #printing the total kg of tomatoes the customer can buy with the budget amount
    
    
#for budget 0
#Enter your budget : 0
#You cannot buy vegetables
#for budget above 100
#Enter your budget : 175
#Total kg of onions you can buy within your budget:  8 kg
#or
#Total kg of tomatoes you can buy within your budget:  16 kg
##for budget 500
#Enter your budget : 500
#Total kg of onions you can buy within your budget:  25 kg
#or
#Total kg of tomatoes you can buy within your budget:  47 kg
