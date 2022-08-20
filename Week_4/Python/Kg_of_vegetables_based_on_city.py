tomato_price = 10.5     #price of tomato is 10.5
budget = float(input("Enter your budget : "))       #reading budget from the customer to know how many kg of vegetables the customer can buy with that amount
print("1. Chennai\n2. Trichy\n3. Madurai")          #printing the cities the customer can enter
city = input("Enter your city from one of the above : ")      #reading the city name as the price of onion varies from one city to another
kg_of_onions = 0        #initializing total kg of onions to 0
kg_of_tomatoes = 0      #initializing total kg of tomatoes to 0

if(budget == 0):        #using if to check whether the budget if 0
    print("You cannot buy vegetables")      #printing that customer cannot buy any vegetables
else:                           #using else to calculate the number of kgs the customer can buy
    if(city == "Chennai"):      #using if loop to check whether the customer entered city as Chennai
        onion_price = 30.0      #since the customer entered city as chennai, we aer initializing price of onion to 30.0
        while(onion_price <= budget):     #using while loop to calculate the price of onion alongside increasing its quantity by 1kg
            onion_price += 30.0     #increasing the price of onions by the price amount for 1 kg
            kg_of_onions += 1       #increasing the quantity of onions 1kg at a time
    elif(city == "Trichy"):     #using if loop to check whether the customer entered city as Trichy
        onion_price = 27.0      #since the customer entered city as trichy, we aer initializing price of onion to 27.0
        while(onion_price <= budget):     #using while loop to calculate the price of onion alongside increasing its quantity by 1kg
            onion_price += 27.0     #increasing the price of onions by the price amount for 1 kg
            kg_of_onions += 1       #increasing the quantity of onions 1kg at a time
    elif(city == "Madurai"):        #using if loop to check whether the customer entered city as Madurai
        onion_price = 34.0      #since the customer entered city as madurai, we aer initializing price of onion to 34.0 
        while(onion_price <= budget):     #using while loop to calculate the price of onion alongside increasing its quantity by 1kg
            onion_price += 34.0     #increasing the price of onions by the price amount for 1 kg
            kg_of_onions += 1       #increasing the quantity of onions 1kg at a time

    while(tomato_price <= budget):        #using while loop to calculate the price of tomato when increasing its quantity by 1kg
        tomato_price += 10.5        #increasing the price of tomatoes by the price amount for 1 kg
        kg_of_tomatoes += 1         #increasing the quantity of tomatoes 1kg at a time

    print("Total kg of onions you can buy within your budget: ", kg_of_onions, "kg")        #printing the total kg of onion the customer can buy with the budget amount
    print("Total kg of tomatoes you can buy within your budget: ", kg_of_tomatoes, "kg")    #printing the total kg of tomatoes the customer can buy with the budget amount