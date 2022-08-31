word = input("Enter a word : ")     #reading input from the user
first_index = None                  #initializing first index as none
last_index = None                   #initializing last index as none

for letter in range(len(word)):         #iterating the input word
    if(word[letter] == "A" or word[letter] == "a" and first_index == None): #checking if the current letter is (A or a) and first index is not found
        first_index = letter                #assigning the current index value as the first index
    elif(word[letter] == "A" or word[letter] == "a"):       #checking if the current letter is A or a
        last_index = letter                               #assigning the current index value as the last index
        break                               #using break as we have found the second occurence of A or a

if(first_index == None):                    #checking whether the first index has not been found
    print("There is no A or a")
elif(last_index == None):                   #checking whether the last index has not been found
    print("There is only one A or a")
else:
    if(first_index + 1 == last_index):      #checking whether the ending index is next to the starting index
        print("There is no letter between first and last A/a")
    else:
        print("Letters between first A/a and last A/a")
        for letter in range(first_index + 1, last_index):   #using for to print the letters between the first and second occurence of A or a
            print(word[letter])                             #printing the letters



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