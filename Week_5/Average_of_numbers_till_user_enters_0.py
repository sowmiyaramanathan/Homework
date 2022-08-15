number = int(input("Enter a number : "))
total_numbers = 0
sum_of_numbers = 0

while(number != 0):
    total_numbers += 1
    sum_of_numbers += number
    number = int(input("Enter a number : "))

if(sum_of_numbers==0):
    print("Average is null")
else:
    average_of_numbers = sum_of_numbers/total_numbers
    print("Average of the given numbers is : ", average_of_numbers)