number_in_numeric = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']      #initializing a list with numeric values of numbers
number_in_english = ["Zero", "One", "Two", "Three", "Four","Five", "Six", "Seven", "Eight", "Nine"] #initializing a list with english names of numbers

number = str(input("Enter a number : "))    #reading a number from the user in string type to iterate through it

for num1 in range(0, len(number)):          #using for to iterate through the input to consider them individually
    for num2 in range(len(number_in_numeric)):          #using for to iterate through the list numeric values
        if(number[num1] == number_in_numeric[num2]):    #using if to check whether the char in input is same as the numeric value in the list
            print(number_in_english[num2], end = '')    #printing the english name of the number in its corresponding position
            break                                       #using break to come out of the inner loop as there is no need to compare with the rest of the items



# test case 1
# Enter a number : 134
# OneThreeFour

# test case 2
# Enter a number : 102478
# OneZeroTwoFourSevenEight

# test case 3
# Enter a number : 000
# ZeroZeroZero

# test case 4
# Enter a number : 234
# TwoThreeFour

# test case 5
# Enter a number : 10501
# OneZeroFiveZeroOne