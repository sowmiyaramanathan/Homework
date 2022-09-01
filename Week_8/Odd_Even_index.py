word = input("Enter a word : ")     #reading input

print("Letter in odd index : ")
for letter in range(1, len(word), 2):       #iterating through the word by odd index
    print(word[letter], end = "")           #printing the letter

print("\nLetter in even index : ")
if(len(word) % 2 == 0):             #checking whether the length of the word is even to fix the starting index
    for letter in range(len(word)-2, -1, -2):       #iterating through the word by even index
        print(word[letter], end = "")               #printing the letter
else:
    for letter in range(len(word)-1, -1, -2):       #iterating through the word by even index
        print(word[letter], end = "")               #printing the letter



"""
test case 1
Enter a word : abcd
Letter in odd index : 
bd
Letter in even index : 
ca

test case 2
Enter a word : Apple
Letter in odd index : 
pl
Letter in even index :
epA

test case 3
Enter a word : Apple#Google
Letter in odd index : 
pl#oge
Letter in even index :
loGepA
"""