word = input("Enter a word : ")     #reading input

odd_index = []
even_index = []

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
Enter a word : abcd
Letter in odd index : 
bd
Letter in even index :
ca

test case 2
Enter a word : Apple
Letters in odd index : 
pl
Letters in even index :
epA

test case 3
Enter a word : Apple#Google
Letters in odd index : 
pl#oge
Letters in even index : 
loGepA
"""