word = input("Enter a word : ")  #reading input from the user
first_A = False     #initializing a boolean value to check whether it is first or last occurence of the letter A
first_A_index = None               #initailzing first index of A as 0
last_A_index = None                #initailzing last index of A as length of the input

for letter in range(len(word)):     #using for to iterate through the input
    if(word[letter] == "A" and first_A == False):   #using if to check whether the cuurent element is A and the first occurence of A is not happened
        first_A_index = letter          #assigning the index position needed to print the output as the current loop variable
        first_A = True             #changing the boolean values as we have found the first index of occurence of A
    elif(word[letter] == "A"):      #using elif to check whether the cuurent element is A to find the last occurence of A
        last_A_index = letter           #assigning the index position needed to print the output as the current loop variable

if(first_A_index == None):
    print("There is no A.")
elif(last_A_index == None):
    print("There is only one A.")
else:
    if(first_A_index + 1 == last_A_index):
        print("No letter between first and last A")
    else:
        print("Letter between first and last A")
        for letter in range(first_A_index + 1, last_A_index):       #using for to print the letters between the first and last occurence of A
            print(word[letter])                                     #printing the letters



# test case 1
# Tree
# There is no A.

# test case 2
# Enter a word : Amazing
# There is only one A.

# test case 3
# Enter a word : Banana
# There is no A.

# test case 4
#Letter between first and last A
# Enter a word : BANANA
# N
# A
# N