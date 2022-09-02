word = input("Enter a word : ")     #reading input
odd_index = []
even_index = []

print("\nLetters in even index : ")
for letter in range(0, len(word)):       #iterating through the word by odd index
    if(letter%2 == 0):
        even_index.insert(0, word[letter])
    else:
        odd_index.append(word[letter])

print("Letters in odd index : ")
print(*odd_index, sep = "")
print("Letters in even index : ")
print(*even_index, sep = "")



"""
test case 1
Enter a word : ABCD1234

Letters in even index :
Letters in odd index :
BD24
Letters in even index :
31CA
_______________________________

test case 2
Enter a word : abcd

Letters in even index :
Letters in odd index :
bd
Letters in even index :
ca
______________________________

test case 3
Enter a word : abc12

Letters in even index :
Letters in odd index :
b1
Letters in even index :
2ca
"""