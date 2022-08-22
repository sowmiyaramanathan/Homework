fruits = ["apple", "orange", "lemon", "mango", "melon"]
supply = [100, 100, 100, 100, 100]
price_of_fruits = [25, 15, 10, 10, 10]
days = ["Monday", "Tuesday", "Wednesday"]

for day in range(len(days)):
    if(days[day] == "Monday"):
        sales = [0, 0, 0, 0, 0]
        print("Sale on monday: ")
        for fruit in range(len(fruits)):
            if(fruits[fruit] == "apple" or fruits[fruit] == "orange"):
                on_monday = 50
                fruits_sold = supply[fruit] - ((supply[fruit] * on_monday) / 100)
                fruits_sold = round(fruits_sold)
                supply[fruit] -= fruits_sold
                amount_earned = fruits_sold * price_of_fruits[fruit]
                sales[fruit] += amount_earned
            else:
                on_monday = 10
                fruits_sold = on_monday
                supply[fruit] -= fruits_sold
                amount_earned = fruits_sold * price_of_fruits[fruit]
                sales[fruit] += amount_earned
            print("Sale in", fruits[fruit], " - Rs.", sales[fruit])

    elif(days[day] == "Tuesday"):
        sales = [0, 0, 0, 0, 0]
        print("Sale on tuesday: ")
        for fruit in range(len(fruits)):
            if(fruits[fruit] == "apple"):
                fruits_sold = supply[fruit]
                supply[fruit] -= fruits_sold
                amount_earned = fruits_sold * price_of_fruits[fruit]
                sales[fruit] += amount_earned
            elif(fruits[fruit] == "orange"):
                on_tuesday = 75
                fruits_sold = supply[fruit] - ((supply[fruit] * on_tuesday) / 100)
                fruits_sold = round(fruits_sold)
                supply[fruit] -= fruits_sold
                amount_earned = fruits_sold * price_of_fruits[fruit]
                sales[fruit] += amount_earned
            else:
                on_tuesday = 30
                fruits_sold = on_tuesday
                supply[fruit] -= fruits_sold
                amount_earned = fruits_sold * price_of_fruits[fruit]
                sales[fruit] += amount_earned
            print("Sale in", fruits[fruit], " - Rs.", sales[fruit])
    
    elif(days[day] == "Wednesday"):
        sales = [0, 0, 0, 0, 0]
        print("Sale on wednesday: ")
        for fruit in range(len(fruits)):
            fruits_sold = supply[fruit]
            supply[fruit] -= fruits_sold
            amount_earned = fruits_sold * price_of_fruits[fruit]
            sales[fruit] += amount_earned
            print("Sale in", fruits[fruit], " - Rs.", sales[fruit])



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