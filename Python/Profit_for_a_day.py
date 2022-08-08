amount_spent_on_employees = 200     #initializing employee salary as 200
amount_spent_on_cakes = 0       #initializing amount spent for cakes as 0 since we do not know it already
amount_spent_on_breads = 0      #initializing amount spent for bread as 0 since we do not know it already
amount_earned_on_cake = 0       #initializing amount gained from cakes as 0 since we do not know it already
amount_earned_on_bread = 0      #initializing amount gained from bread as 0 since we do not know it already
total_amount_earned = 0         #initializing total amount earned as 0 since we do not know it already
total_amount_spent = 0      #initializing total amount spent as 0 since we do not know it already
profit_for_a_day = 0        #initializing profit of the day as 0 since we do not know it already

for i in range(1,11):       #using for loop from 1 to 10 since 10 customers are coming to the shop every day
    item = input("What did the customer bought? Cake / Bread : ")       #reading what the customer would like to buy
    if(item == "Cake"):                                                 #using if statement to check if the customer need cakes
        number_of_cake = int(input("Enter the number of cakes: "))      #reading number of cake the customer wants
        amount_earned_on_cake = amount_earned_on_cake + (number_of_cake * 40)   #calculating amount earned on cakes by multiplying number of cake with 40 and adding it with amount earned on cake 
        amount_spent_on_cakes = amount_spent_on_cakes + (number_of_cake * 20)   #calculating amount spent on cakes by multiplying number of cake with 20 and adding it with amount spent on cake 
    if(item == "Bread"):                                                #using if statement to check if the customer need bread
        number_of_bread = int(input("Enter the number of bread: "))     #reading number of bread the customer wants
        amount_earned_on_bread = amount_earned_on_bread + (number_of_bread * 15)    #calculating amount earned on bread by multiplying number of bread with 15 and adding it with amount earned on bread 
        amount_spent_on_breads = amount_spent_on_breads + (number_of_bread * 10)    #calculating amount spent on bread by multiplying number of bread with 10 and adding it with amount spent on bread 

total_amount_earned = amount_earned_on_cake + amount_earned_on_bread        #calculating total amount earned by adding the amounts earned on cake and bread
total_amount_spent = amount_spent_on_cakes + amount_spent_on_breads + amount_spent_on_employees     #calculating total amount spent by adding the amounts spent on cake, bread, and, salary
profit_for_a_day = total_amount_earned - total_amount_spent     #calculating total profit for the day by subtracting total amount spent from total amount earned

print("Profit for the day: ", profit_for_a_day)     #printing total profit for the day