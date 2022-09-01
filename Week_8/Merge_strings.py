firstWord = input("Enter first word : ")            #reading first word
secondWord = input("Enter second word : ")          #reading second word

mergedWord = firstWord + secondWord                 #merging two words and storing it in a variable

#printing the results
print("Before merging")
print("First word : ", firstWord)
print("Second word : ", secondWord)
print("\nAfter merging")
print("Merged word : ", mergedWord)



"""
test case 1
Enter first word : Hello
Enter second word : Welcome
Before merging
First word :  Hello
Second word :  Welcome

After merging
Merged word :  HelloWelcome
---------------------------------

test case 2
Enter first word : 1234
Enter second word : abcd
Before merging
First word :  1234
Second word :  abcd

After merging
Merged word :  1234abcd
----------------------------------

test case 3
Enter first word : Micro
Enter second word : soft

Before merging
First word :  Micro
Second word :  soft
After merging
Merged word :  Microsoft
"""