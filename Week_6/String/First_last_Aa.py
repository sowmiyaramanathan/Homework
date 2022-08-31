word = input("Enter a word : ")         #reading input from the user
first_index = None                      #initializing first index as none
last_index = None                       #initializing last index as none

for letter in range(len(word)):         #iterating the input word
    if(word[letter] == "A" or word[letter] == "a" and first_index == None): #checking if the current letter is (A or a) and first index is not found
        first_index = letter                    #assigning the current index value as the first index
    elif(word[letter] == "A" or word[letter] == "a"):       #checking if the current letter is A or a iteratively to find the last occurence of A or a
        last_index = letter                               #assigning the current index value as the last index

if(first_index == None):                #checking whether the first index has not been found
    print("No A/a is found")
elif(last_index == None):               #checking whether the last index has not been found
    print("There is only one A/a")
else:
    if(first_index + 1 == last_index):  #checking whether the ending index is next to the starting index
        print("No letters between first and last A or a")
    else:
        print("Letter between first and last A/a")
        for letter in range(first_index + 1, last_index):   #using for to print the letters between the first and last occurence of A or a
            print(word[letter])                             #printing the letters



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