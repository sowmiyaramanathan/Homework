number = int(input("Enter a number (to end, enter 0): "))    #reading a number from the user to see if we can continue reading next numbers
total_numbers = 0                           #initializing total numbers to 0
sum_of_numbers = 0                          #initializing sum of all numbers to 0

if(number == 0):              #using if to check whether user has entered 0 at the very beginning
    print("Average is null")        #printing that there is no average
else:
    while(number != 0):           #using while to continue reading numbers from the user till the user enters 0 as input
        total_numbers += 1           #increasing total numbers by 1
        sum_of_numbers += number     #calculating sum of numbers by adding sum of numbers with the input number
        number = int(input("Enter a number (to end, enter 0): "))       #reading for next input from the user
    average_of_numbers = sum_of_numbers / total_numbers       #calculating average by dividing sum of numbers by total numbers
    print("Average of the given numbers is : ", average_of_numbers)     #printing the average of input numbers
    
    
    
#for number 0
#Enter a number (to end, enter 0): 0
#Average is null

#test case with negative number
#Enter a number (to end, enter 0): 5
#Enter a number (to end, enter 0): -8
#Enter a number (to end, enter 0): 9
#Enter a number (to end, enter 0): -1
#Enter a number (to end, enter 0): 3
#Enter a number (to end, enter 0): 4
#Enter a number (to end, enter 0): 0
#Average of the given numbers is :  2.0

#test case with negative number
#Enter a number (to end, enter 0): -9
#Enter a number (to end, enter 0): -8
#Enter a number (to end, enter 0): 5
#Enter a number (to end, enter 0): 0
#Average of the given numbers is :  -4.0
