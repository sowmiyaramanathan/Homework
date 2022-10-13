import random
from numpy import size

def generateWord(size):
    generatedWord = random.choice(open(r"C:\Users\user\Desktop\Sayur Learning\Sowmiya\Week_15\WordleInput.txt").read().split())
    while len(generatedWord) != size:
        generatedWord = random.choice(open(r"C:\Users\user\Desktop\Sayur Learning\Sowmiya\Week_15\WordleInput.txt").read().split())
    return generatedWord

def getWord(wordLength):
    print("Shot your guess : ")
    guessedWord = input()
    if(len(guessedWord) != wordLength):
        guessedWord = input("Enter a " + str(wordLength) + " letter word : ")
    return guessedWord

def checkWords(inputWord, actualWord, wordSize):
    tempList = []
    checkString = "B" * wordSize
    checkString = list(checkString)
    for char in range(wordSize):
        if actualWord[char] == inputWord[char]:
            checkString[char] = "G"
            tempList.append(actualWord[char])
    for char in range(wordSize):
        if inputWord[char] in actualWord and checkString[char] != "G" and inputWord[char] not in tempList:
            checkString[char] = "Y"
    
    for char in range(wordSize):
        if inputWord[char] not in actualWord:
            checkString[char] = "B"

    print(''.join([str(i) for i in checkString]))


goForNextRound = True
wordSize = 3

while wordSize <= 5 and goForNextRound == True:
    print("WELCOME TO WORDLE")
    actualWord = generateWord(wordSize)
    maxChance = 5
    while maxChance > 0:
        inputWord = getWord(len(actualWord))
        checkWords(inputWord, actualWord, len(actualWord))
        if inputWord == actualWord:
            print("You won")
            goForNextRound = True
            maxChance = 0
        else:
            goForNextRound = False
            maxChance -= 1
    wordSize += 1
    if maxChance == 0 and goForNextRound == False:
        print("Try agian next time")
        exit()