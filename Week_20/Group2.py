actualWord = list("hello")
guessedWord = list("llloo")

for i in range(0, len(actualWord)):
    if guessedWord[i] == actualWord[i]:
        print("Green ")
    elif guessedWord[i] in actualWord:
        if guessedWord.count(guessedWord[i]) == actualWord.count(guessedWord[i]):
            print("Yellow ")
            guessedWord[i] = "?"
        else:
            guessedWord[i] = "?"
            print("red ")
    else:
        print("red ")