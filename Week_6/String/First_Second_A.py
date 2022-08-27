word = input("Enter a word : ")
first_index = None
last_index = None

for letter in range(len(word)):
    if(word[letter] == "A" or word[letter] == "a" and first_index == None):
        first_index = letter
    elif(word[letter] == "A" or word[letter] == "a"):
        last_index = letter
        break

if(first_index == None):
    print("There is no A or a")
elif(last_index == None):
    print("There is only one A or a")
else:
    if(first_index + 1 == last_index):
        print("There is no letter between first and last A/a")
    else:
        print("Letters between first A/a and last A/a")
        for letter in range(first_index + 1, last_index):
            print(word[letter])


"""
test case 1
Enter a word : Amanda
Letters between first A/a and last A/a
m

test case 2
Enter a word : Animals
Letters between first A/a and last A/a
n
i
m

test case 3
Enter a word : London
There is no A or a

test case 4
Enter a word : Programming
There is only one A or a
"""