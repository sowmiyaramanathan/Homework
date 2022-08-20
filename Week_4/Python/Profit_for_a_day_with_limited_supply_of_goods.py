amount_spent_on_employees = 200     #initializing employee salary as 200
amount_spent_on_cakes = 0       #initializing amount spent for cakes as 0 since we do not know it already
amount_spent_on_breads = 0      #initializing amount spent for bread as 0 since we do not know it already
amount_earned_on_cake = 0       #initializing amount gained from cakes as 0 since we do not know it already
amount_earned_on_bread = 0      #initializing amount gained from bread as 0 since we do not know it already
total_amount_earned = 0     #initializing total amount earned as 0 since we do not know it already
total_amount_spent = 0      #initializing total amount spent as 0 since we do not know it already
profit_for_a_day = 0        #initializing profit of the day as 0 since we do not know it already

supply_of_cake = int(input("Enter the supply of cake : "))          #reading supply of cake
supply_of_bread = int(input("Enter the supply of bread : "))        #reading supply of bread

while(supply_of_cake > 0 or supply_of_bread > 0):                           #using while to check if supply of cake or supply of bread is greater than 0 to take in orders from the customer
    item = input("What did the customer bought? Cake / Bread : ")       #reading what the customer would like to buy
    if(item == "Cake"):                                          #using if statement to check if the customer need cakes
        number_of_cake = int(input("Enter the number of cakes: "))      #reading number of cake the customer wants
        if(number_of_cake <= supply_of_cake):                             #using if to check if number of cakes the customer wants is less than or equal to the supply of cakes
            amount_earned_on_cake = amount_earned_on_cake + (number_of_cake * 40)   #calculating amount earned on cakes by multiplying number of cake with 40 and adding it with amount earned on cake 
            amount_spent_on_cakes = amount_spent_on_cakes + (number_of_cake * 20)   #calculating amount spent on cakes by multiplying number of cake with 20 and adding it with amount spent on cake 
            supply_of_cake -= number_of_cake                     #reducing the supply of cake in stock by the number of cakes in the last order
        else:                                                    #using else to indicate the customer that the supply of cake is not sufficient to take the order
            print("No sufficient cake in stock. Available number of bread : ", supply_of_cake)   #printing that the supply of cake is not sufficient
    if(item == "Bread"):                                         #using if statement to check if the customer need bread
        number_of_bread = int(input("Enter the number of bread: "))     #reading number of bread the customer wants
        if(number_of_bread <= supply_of_bread):                           #using if to check if number of bread the customer wants is less than or equal to the supply of bread
            amount_earned_on_bread = amount_earned_on_bread + (number_of_bread * 15)    #calculating amount earned on bread by multiplying number of bread with 15 and adding it with amount earned on bread 
            amount_spent_on_breads = amount_spent_on_breads + (number_of_bread * 10)    #calculating amount spent on bread by multiplying number of bread with 10 and adding it with amount spent on bread 
            supply_of_bread -= number_of_bread                          #reducing the supply of bread in stock by the number of bread in the last order
        else:                                              #using else to indicate the customer that the supply of bread is not sufficient to take the order
            print("No sufficient bread in stock. Available number of bread : ", supply_of_bread)  #printing that the supply of bread is not sufficient

total_amount_earned = amount_earned_on_cake + amount_earned_on_bread        #calculating total amount earned by adding the amounts earned on cake and bread
total_amount_spent = amount_spent_on_cakes + amount_spent_on_breads + amount_spent_on_employees     #calculating total amount spent by adding the amounts spent on cake, bread, and, salary
profit_for_a_day = total_amount_earned - total_amount_spent     #calculating total profit for the day by subtracting total amount spent from total amount earned

print("Profit for the day: ", profit_for_a_day)     #printing total profit for the day