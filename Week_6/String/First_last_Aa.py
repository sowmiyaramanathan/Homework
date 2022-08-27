word = input("Enter a word : ")
first_index = None
last_index = None

for letter in range(len(word)):
    if(word[letter] == "A" or word[letter] == "a" and first_index == None):
        first_index = letter
    elif(word[letter] == "A" or word[letter] == "a"):
        last_index = letter

if(first_index == None):
    print("No A/a is found")
elif(last_index == None):
    print("There is only one A/a")
else:
    if(first_index + 1 == last_index):
        print("No letters between first and last A or a")
    else:
        print("Letter between first and last A/a")
        for letter in range(first_index + 1, last_index):
            print(word[letter])



"""
test case 1
Enter a word : Assignment
There is only one A/a

test case 2
Enter a word : Everyone
No A/a is found

test case 3
Enter a word : Amanda
Letter between first and last A/a
m
a
n
d """