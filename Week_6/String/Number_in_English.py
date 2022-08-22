number_in_numeric = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
number_in_english = ["Zero", "One", "Two", "Three", "Four","Five", "Six", "Seven", "Eight", "Nine"]

number = str(input("Enter a number : "))

for num1 in range(0, len(number)):
    for num2 in range(len(number_in_numeric)):
        if number[num1] == number_in_numeric[num2]:
            print(number_in_english[num2], end = '')
            break



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