number_in_numeric = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']      #initializing a list with numeric values of numbers
number_in_english = ["Zero", "One", "Two", "Three", "Four","Five", "Six", "Seven", "Eight", "Nine"] #initializing a list with english names of numbers
number = int(input("Enter a number : "))                                #reading a number from the user
number_string = str(number)                             #converting the number into a string to iterate through it

for num1 in range(len(number_string)):                              #using for to iterate through the input
    if number_string[num1] in number_in_numeric:            #using if to check whether the single unit of the input is in the numeric list
        index_position = number_in_numeric.index(number_string[num1])       #finding the index position of the numeric list
        print(number_in_english[index_position], end = '')          #printing the number in words using the index position



# test case 1
# Enter a number : 134
# OneThreeFour

# test case 2
# Enter a number : 102478
# OneZeroTwoFourSevenEight

# test case 3
# Enter a number : 000
# Zero

# test case 4
# Enter a number : 257
# TwoFiveSeven

# test case 5
# Enter a number : 10501
# OneZeroFiveZeroOne