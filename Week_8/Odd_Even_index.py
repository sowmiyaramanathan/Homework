word = input("Enter a word : ")

print("Letter in odd index : ")
for letter in range(1, len(word), 2):
    print(word[letter], end = "")

print("\nLetter in even index : ")
if(len(word) % 2 == 0):
    for letter in range(len(word)-2, -1, -2):
        print(word[letter], end = "")
else:
    for letter in range(len(word)-1, -1, -2):
        print(word[letter], end = "")