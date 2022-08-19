number = int(input("Enter a number (to end, enter 0): "))    #reading a number from the user to see if we can continue reading next numbers
total_numbers = 0                           #initializing total numbers to 0
sum_of_numbers = 0                          #initializing sum of all numbers to 0

while(number != 0):              #using while to continue reading numbers from the user till the user enters 0 as input
    total_numbers += 1           #increasing total numbers by 1
    sum_of_numbers += number     #calculating sum of numbers by adding sum of numbers with the input number
    number = int(input("Enter a number (to end, enter 0): "))       #reading for next input from the user

if(sum_of_numbers == 0):              #if the user has entered 0 at the very beginning, sum of numbers will be 0. So when printing average, there will be run time error. To tackle that, we handle that by an if statement that checks whether the sum of number is 0
    print("Average is null")        #printing that there is no average
else:                               #using else to print the average
    average_of_numbers = sum_of_numbers/total_numbers       #calculating average by dividing sum of numbers by total numbers
    print("Average of the given numbers is : ", average_of_numbers)     #printing the average of input numbers