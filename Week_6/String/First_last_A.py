word = input("Enter a word that consists of atleast two A's in it : ")
first_A = False

for letter in range(len(word)):
    if(word[letter] == "A" and first_A == False):
        first_A = True
        first_A_index = letter
    elif(word[letter] == "A" and first_A == True):
        last_A_index = letter
        break

for letter in range(first_A_index + 1, last_A_index):
    print(word[letter])



# test case 2
# AEROPLANE
# E
# R
# O
# P
# L

# test case 2
# Enter a word that consists of atleast two A's in it : UNITED STATES OF AMERICA
# T
# E
# S
#
# O
# F
#