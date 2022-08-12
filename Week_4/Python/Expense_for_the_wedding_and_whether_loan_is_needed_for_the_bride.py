lunch_cost_per_person = int(input("Enter the lunch cost per person : "))        #reading lunch cost for a person
breakfast_cost_per_person = lunch_cost_per_person / 2                #calculating breakfast cost for a person which is half of lunch per person
hall_cost_per_person = lunch_cost_per_person / 3                    #calculating hall cost for a person which is one third of lunch per person
parking_cost_per_person = hall_cost_per_person - ((hall_cost_per_person * 10) / 100)    #calculating parking cost for a person which is 3 percent of hall cost
total_cost_per_person = lunch_cost_per_person + breakfast_cost_per_person + hall_cost_per_person + parking_cost_per_person  #calculating total expense for a person by adding lunch, breakfast, hall, and parking cost

number_of_persons = int(input("Enter the number of persons : "))        #reading number of persons expected to attend the wedding
total_cost_for_all_persons = total_cost_per_person * number_of_persons  #calculating expense for the number of persons who are expected to attend the wedding

decoration_cost = (hall_cost_per_person * number_of_persons) / 2        #calculating decoration cost which is half of hall cost. Since decoraion cost is half of hall cost of one person, we are multiply the hall cost of one person with total number of persons expected to the wedding and then dividing it with to get the half of total hall cost

total_expense_for_the_wedding = total_cost_for_all_persons + decoration_cost    #calculating total expense for the wedding by adding total cost for the expected persong and decoration cost

amount_to_be_spent_by_the_bride = total_expense_for_the_wedding / 2             #calculating amount to be spent by the bride by dividing it by 2 as the expense for the wedding is equally split between the bride and the groom
amount_saved_by_the_bride = 50000                                   #initialising amount saved by the bride to 50000 as given in the problem

if(amount_to_be_spent_by_the_bride>amount_saved_by_the_bride):      #using if to check whether amount to be spent by the bride is greater than the amount saved by the bride to calculate amount needed by the bride
    amount_needed_by_the_bride = amount_to_be_spent_by_the_bride - amount_saved_by_the_bride    #calculating amount needed by the bride by subtracting amount saved by the bride from amount to be spent
    print("The bride needs loan. And the loan amount is ", amount_needed_by_the_bride)          #printing amount needed by the bride
else:                                               #using else to let know that the bride has sufficient amount and doesn't need extra amount
    print("The bride does not need a loan.")        #printing that the bride doesn't a loan