import random                                       #importing radom package

def generateRandomNumber(number, start, end):       #function to get a number that is always divisibke by the input number
    if number > end:                                #checking whether number is less than limit
        print("Enter a number below ", end)         #printing enter below limit
    elif number <= 0:                               #checking whether number is less than or equal to 0
        print("Enter a number above 0")             #printing enter above 0
    else:
        randomNumber = random.randint(start, end)   #generating a random number
        while randomNumber % number != 0:           #till the generated number is divisible by the input number
            randomNumber = random.randint(start, end)   #generate a random number
        print("Number divisible by ", number, " is : ", randomNumber)       #printing the resultant random number

inputNumber = int(input("Enter a number (below 1000): "))           #reading the input number from the user
startValue = 1                                                      #setting start limit
endValue = 1000                                                     #setting end limit
generateRandomNumber(inputNumber, startValue, endValue)             #calling function to generate a number that is always divisible by the input number


"""
test case 1
Enter a number (below 1000): 5
Number divisible by  5  is :  670

test case 2
Enter a number (below 1000): 2000
Enter a number below  1000

test case 3
Enter a number (below 1000): 500
Number divisible by  500  is :  1000

test case 4
Enter a number (below 1000): 0
Enter a number above 0

test case 5
Enter a number (below 1000): 100
Number divisible by  100  is :  100

test case 6
Enter a number (below 1000): 100
Number divisible by  100  is :  400
"""