from re import L


word = input("Enter a word : ")     #reading input
letter1 = input("Enter a letter to be replaced : ")     #reading letter to be replaced
letter2 = input("Enter a letter to replace : ")         #reading letter to replace

replaced_word = ""                                      #initializing a string variable to store the output
same_letter = False               #initializing a boolean value to track if there is a match in the input

for letter in range(len(word)):                         #using for loop to iterate the given word
    if(word[letter] == letter1):        #using if to compare whether the current letter is same as the letter to be replaced
         replaced_word += letter2                       #adding the word to replace, to the output variable
         same_letter = True                         #changing the boolean to know that there is a match
    else:                               #using else to handle the not equal condition of the if statement
        replaced_word += word[letter]   #adding the current word, to the output variable

if(same_letter == True):                    #chekcing the boolean value for matching of the inputs
    print("Before replacing :")
    print(word)                             #printing the original word
    print("After replacing : ")
    print(replaced_word)                    #printing the replaced word
else:                                       #using else to print if there is no match in the input
    print("There is no ", letter1, " in the given word")

"""
test case 1
Enter a word : Apple
Enter a letter to be replaced : e
Enter a letter to replace : 
Before replacing :
Apple
After replacing :
Appl

test case 2
Enter a word : Microsoft
Enter a letter to be replaced : a
Enter a letter to replace : q
There is no  a  in the given word
"""