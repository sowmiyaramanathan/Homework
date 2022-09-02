word = input("Enter a word : ")     #reading input

odd_index = []                      #initializing a list to store elements in odd index
even_index = []                     #initializing a list to store elements in even index

for letter in range(0, len(word)):          #iterating through the word
    if(letter%2 == 0):                      #checking whether the current index is even
        even_index.insert(0, word[letter])      #adding the current element to even list
    else:
        odd_index.append(word[letter])          #in case of odd, adding the current element to odd list

print("Letters in odd index : ")
print(*odd_index, sep = "")                     #printing elements in odd index
print("Letters in even index : ")
print(*even_index, sep = "")                    #printing elements in even index



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