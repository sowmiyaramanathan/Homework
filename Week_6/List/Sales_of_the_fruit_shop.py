fruits = ["apple", "orange", "lemon", "mango", "melon"]     #initializing a list with fruits
supply = [100, 100, 100, 100, 100]                          #initializing the supply of the fruits
price_of_fruits = [25, 15, 10, 10, 10]                      #initializing the price of the fruits
days = ["Monday", "Tuesday", "Wednesday"]                   #initializing the days given in the problem

for day in range(len(days)):                            #using for to loop through the days list
    if(days[day] == "Monday"):                          #using if to check whether the day is monday
        sales = [0, 0, 0, 0, 0]                         #initializing sales for that particular day
        print("Sale on monday: ")                       #printing sales on monday
        for fruit in range(len(fruits)):                #using for to iterate through the fruits list
            if(fruits[fruit] == "apple" or fruits[fruit] == "orange"):      #using if to check whether the fruit is apple or orange
                on_monday = 50                          #initializing sales percentage of the fruit as 50
                fruits_sold = supply[fruit] - ((supply[fruit] * on_monday) / 100)   #calculating fruits sold which is 50% of its supply
                fruits_sold = round(fruits_sold)        #making the number of vegetables as a whole number
                supply[fruit] -= fruits_sold            #updating supply by subtracting the fruits sold from supply of the fruit
                amount_earned = fruits_sold * price_of_fruits[fruit]    #calculating amount earned by multiplying fruits sold by price of the fruit
                sales[fruit] += amount_earned           #updating the sales list with the amount earned value
            else:                                       #using else to calculate sales for other fruits
                on_monday = 10                          #initializing the number of fruits sold on monday as 10
                fruits_sold = on_monday                 #assigning the sale number on monday to fruits sold
                supply[fruit] -= fruits_sold            #updating supply by subtracting the fruits sold from supply of the fruit
                amount_earned = fruits_sold * price_of_fruits[fruit]    #calculating amount earned by multiplying fruits sold by price of the fruit
                sales[fruit] += amount_earned           #updating the sales list with the amount earned value
            print("Sale in", fruits[fruit], " - Rs.", sales[fruit])     #printing the sales for monday

    elif(days[day] == "Tuesday"):                       #using elif to check whether the day is tuesday
        sales = [0, 0, 0, 0, 0]                         #initializing sales for that particular day
        print("Sale on tuesday: ")                      #printing sales on tuesday
        for fruit in range(len(fruits)):                #using for to iterate through the fruits list
            if(fruits[fruit] == "apple"):               #using if to check whether the fruit is apple
                fruits_sold = supply[fruit]             #since all the remaining apples are sold on tuesday, assigning fruits sold as supply of fruit
                supply[fruit] -= fruits_sold            #updating supply by subtracting the fruits sold from supply of the fruit
                amount_earned = fruits_sold * price_of_fruits[fruit]    #calculating amount earned by multiplying fruits sold by price of the fruit
                sales[fruit] += amount_earned           #updating the sales list with the amount earned value
            elif(fruits[fruit] == "orange"):            #using elif to check whether the fruit is orange
                on_tuesday = 75                         #initializing sales percentage of the fruit as 75
                fruits_sold = supply[fruit] - ((supply[fruit] * on_tuesday) / 100)     #calculating fruits sold which is 75% of its supply 
                fruits_sold = round(fruits_sold)        #making the number of vegetables as a whole number
                supply[fruit] -= fruits_sold            #updating supply by subtracting the fruits sold from supply of the fruit
                amount_earned = fruits_sold * price_of_fruits[fruit]    #calculating amount earned by multiplying fruits sold by price of the fruit
                sales[fruit] += amount_earned           #updating the sales list with the amount earned value
            else:                                       #using else to calculate sales for other fruits
                on_tuesday = 30                         #initializing the number of fruits sold on tuesday as 30
                fruits_sold = on_tuesday                #assigning the sale number on monday to fruits sold
                supply[fruit] -= fruits_sold            #updating supply by subtracting the fruits sold from supply of the fruit
                amount_earned = fruits_sold * price_of_fruits[fruit]    #calculating amount earned by multiplying fruits sold by price of the fruit
                sales[fruit] += amount_earned           #updating the sales list with the amount earned value
            print("Sale in", fruits[fruit], " - Rs.", sales[fruit])     #printing the sales for tuesday
    
    elif(days[day] == "Wednesday"):                     #using elif to check whether the day is wednesday
        sales = [0, 0, 0, 0, 0]                         #initializing sales for that particular day
        print("Sale on wednesday: ")                    #printing sales on tuesday
        for fruit in range(len(fruits)):                #using for to iterate through the fruits list
            fruits_sold = supply[fruit]                 #since all the remaining fruits are sold on wednesday, assigning fruits sold as supply of fruit
            supply[fruit] -= fruits_sold                #updating supply by subtracting the fruits sold from supply of the fruit
            amount_earned = fruits_sold * price_of_fruits[fruit]    #calculating amount earned by multiplying fruits sold by price of the fruit
            sales[fruit] += amount_earned               #updating the sales list with the amount earned value
            print("Sale in", fruits[fruit], " - Rs.", sales[fruit])     #printing the sales for wednesday



# test case 1
# Sale on monday: 
# Sale in apple  - Rs. 1250
# Sale in orange  - Rs. 750
# Sale in lemon  - Rs. 100
# Sale in mango  - Rs. 100
# Sale in melon  - Rs. 100
# Sale on tuesday: 
# Sale in apple  - Rs. 1250
# Sale in orange  - Rs. 180
# Sale in lemon  - Rs. 300
# Sale in mango  - Rs. 300
# Sale in melon  - Rs. 300
# Sale on wednesday: 
# Sale in apple  - Rs. 0
# Sale in orange  - Rs. 570
# Sale in lemon  - Rs. 600
# Sale in mango  - Rs. 600
# Sale in melon  - Rs. 600