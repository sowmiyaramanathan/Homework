first_word = input("Enter a word : ")       #reading a string from the user
second_word = input("Enter a word : ")      #reading another string from the user
same_words = []                  #declaring a list for storing the characters that are present in both the strings
no_same_char = True

for letter1 in range(len(first_word)):          #using for to iterate through the first string
    for letter2 in range(len(second_word)):     #using for to iterate through the second string
        if first_word[letter1] in same_words:   #using if to check whether the character in first string is already present in the same words list to avoid printing the characters again and again
            break                               #using break to come out of the inner loop 
        else:                                   #using else to check for similarity 
            if first_word[letter1] in second_word:      #using if to check whether the current character in first string is same as any character in the second string
                same_words.append(first_word[letter1])   #adding the current character to the corresponding list
                no_same_char = False
if(no_same_char == True):
    print("No same characters")
else:
    print("Common characters in the given words")
    print(*same_words)      #printing the same words list



# test case 1
# Enter a word : BANANA
# Enter a word : banana
# No same characters

# test case 2
# Enter a word : boy in a house
# Enter a word : boy in hotel
# b o y   i n h e

# test case 3
# Enter a word : manchester
# Enter a word : amsterdam
# m a e s t r

# test case 4
# Enter a word : BANANA
# Enter a word : CHERRY
# No same characters