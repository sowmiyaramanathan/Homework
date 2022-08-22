word = input("Enter a word that consists of atleast two A's in it : ")  #reading input from the user
first_A = False     #initializing a boolean value to check whether it is first or last occurence of the letter A
first_A_index = 0               #initailzing first index of A as 0
last_A_index = len(word)        #initailzing last index of A as length of the input

for letter in range(len(word)):     #using for to iterate through the input
    if(word[letter] == "A" and first_A == False):   #using if to check whether the cuurent element is A and the first occurence of A is not happened
        first_A_index = letter          #assigning the index position needed to print the output as the current loop variable
        first_A = True             #changing the boolean values as we have found the first index of occurence of A
    elif(word[letter] == "A"):      #using elif to check whether the cuurent element is A to find the last occurence of A
        last_A_index = letter           #assigning the index position needed to print the output as the current loop variable

for letter in range(first_A_index + 1, last_A_index):       #using for to print the letters between the first and last occurence of A
    print(word[letter])                                     #printing the letters



# test case 1
# Enter a word that consists of atleast two A's in it : UNITED STATES OF AMERICA
# T
# E
# S
#
# O
# F
#
# A
# M
# E
# R
# I
# C

# test case 2
# Enter a word that consists of atleast two A's in it : BANANA
# N
# A
# N

# test case 3
# Enter a word that consists of atleast two A's in it : AMAZING
# M

# test case 4
# Enter a word that consists of atleast two A's in it : AAA
# A

# test case 5
# Enter a word that consists of atleast two A's in it : ABABABAB
# B
# A
# B
# A
# B

# test case 6
# Enter a word that consists of atleast two A's in it : Amazing
# m
# a
# z
# i
# n
# g