word = input("Enter a word : ")
first_index = None
last_index = None

for letter in range(len(word)):
    if(word[letter] == "A" or word[letter] == "a" and first_index == None):
        first_index = letter
    elif(word[letter] == "N" or word[letter] == "a"):
        last_index = letter
        break

if(first_index == None):
    print("There is no A or a")
elif(last_index == None):
        print("There is no N or a to stop printing letters")
else:
    if(first_index+1 == last_index):
        print("No letters between first A/a and first N/a")
    else:
        print("Letter between first A/a and first N/a")
        for letter in range(first_index + 1, last_index):
            print(word[letter])




""" test case 1
Enter a word : Anand  
Letter between first A/a and first N/a
n

test case 2
Enter a word : Hai
There is no N or a to stop printing letters

test case 3
Enter a word : hello
There is no A or a

test case 4
Enter a word : Hall of fame
Letter between first A/a and first N/a
l
l

o
f

f """
