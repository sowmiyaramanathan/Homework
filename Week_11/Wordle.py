import random

def getWord(size):
    randomIndex = random.randint(0, len(wordsList)-1)
    findWord = wordsList[randomIndex]
    while(len(findWord) != size):
        randomIndex = random.randint(0, len(wordsList)-1)
        findWord = wordsList[randomIndex]
    return findWord

def playGame(word):
    global goForNextRound
    totalChance = 5
    while(totalChance>0):
        guessWord = input("Enter a word : ")
        guessWord = guessWord.lower()
        if(len(guessWord) != len(word)):
            guessWord = input("Enter a " + str(len(word)) + "letter word : ")
            guessWord = guessWord.lower()
        for letter in range(len(guessWord)):
            checkPresense = ""
            checkChar1 = guessWord[letter]
            for letter1 in range(len(word)):
                checkChar2 = word[letter1]
                if checkChar1 == checkChar2 and letter == letter1:
                    checkPresense = "G"
                    break
                elif checkChar1 == checkChar2 and letter != letter1:
                    checkPresense = "Y"
                    break
                elif checkChar1 != checkChar2 and letter1 == len(word)-1:
                    checkPresense = "B"
                    break
            print(checkPresense, end = " ")
        print("\n")
        if guessWord.lower() == word.lower():
            print("You won")
            goForNextRound = True
            totalChance = 1
        else:
            goForNextRound = False
        totalChance -= 1
    if(goForNextRound == False):
        print("Try again next time")
        print("The actual word is ", word)

wordsList = ["car", "bat", "gate", "four", "sweet", "night"]
checkPresense = ""
checkSize = 3
goForNextRound = True

while(checkSize <= 5 and goForNextRound == True):
    findWord = getWord(checkSize)
    playGame(findWord)
    checkSize += 1