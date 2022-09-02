firstWord = input("Enter first word : ")            #reading first word
secondWord = input("Enter second word : ")          #reading second word

if(len(firstWord) == len(secondWord)):
    print("Mergrd String:")
    for letter in range(len(firstWord)):
        print(firstWord[letter], end = "")
        print(secondWord[letter], end = "")

else:
    print("The given strings are of different length")




"""
test case 1
Enter first word : abcd
Enter second word : 1234
Mergrd String:
a1b2c3d4
---------------------------------

test case 2
Enter first word : Hello
Enter second word : Welcome
The given strings are of different length
----------------------------------
"""