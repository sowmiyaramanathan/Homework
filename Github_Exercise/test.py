word = input("Enter a word : ")
reversed_word = ""

for letter in range(len(word)-1, -1, -1):
    reversed_word += word[letter]

print(reversed_word)