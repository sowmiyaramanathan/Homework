first_word = input("Enter a word : ")
second_word = input("Enter a word : ")
same_words = []

for letter1 in range(len(first_word)):
    for letter2 in range(len(second_word)):
        if first_word[letter1] in same_words:
            break
        else:
            if first_word[letter1] in second_word:
                same_words.append(first_word[letter1])

print(*same_words)



# test case 1
# Enter a word : BANANA
# Enter a word : banana
#

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
#