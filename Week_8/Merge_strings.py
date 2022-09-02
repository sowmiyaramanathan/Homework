firstWord = input("Enter first word : ")            #reading first word
secondWord = input("Enter second word : ")          #reading second word

if(len(firstWord) == len(secondWord)):              #checking whether the length of the given strings is same
    print("Merged String:")
    for letter in range(len(firstWord)):            #in case of same, iterating through the first input string
        print(firstWord[letter], end = "")
        print(secondWord[letter], end = "")

else:                                               #if not same, printing not same
    print("The given strings are of different length")




"""
test case 1
Enter first word : abcd
Enter second word : 1234
Merged String:
a1b2c3d4
---------------------------------

test case 2
Enter first word : Hello
Enter second word : Welcome
The given strings are of different length
----------------------------------
"""