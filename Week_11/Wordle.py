import random                       #importing random package to help in generating a random word from the list

def getWord(size):                  #function to get a word
    randomIndex = random.randint(0, len(wordsList)-1)           #generting a random number within 0 and the length of the wordlist
    findWord = wordsList[randomIndex]                           #by using the random number as the index, we get the word from the list
    while(len(findWord) != size):                               #till the length of the word is sufficient
        randomIndex = random.randint(0, len(wordsList)-1)       #generating another number
        findWord = wordsList[randomIndex]                       #getting the word
    return findWord                                             #returning the word found

def playGame(word):                             #function to start the game
    global goForNextRound                       #variable to decide whether the player can go to the next level
    totalChance = 5                             #declaring the total chance to 5
    while(totalChance>0):                       #till the total beomes 0 i.e., no further chances are left to continue
        guessWord = input("Enter a word : ")    #getting the input word from the user
        guessWord = guessWord.lower()           #converting the input to small case
        if(len(guessWord) != len(word)):      #when the length of the input is not equal to the length of the actual word
            guessWord = input("Enter a " + str(len(word)) + " letter word : ") #asking the user an input in correct length
            guessWord = guessWord.lower()           #converting the input to small case
        for letter in range(len(guessWord)):        #iterating through the input word
            checkPresense = ""          #for each iteration setting a variable empty to store the correctness input word
            checkChar1 = guessWord[letter]          #accessing a single character from the input word
            for letter1 in range(len(word)):        #iterating through the actual word
                checkChar2 = word[letter1]          #accessing a single character from the actual word
                if checkChar1 == checkChar2 and letter == letter1:  #checking the similarity and index position of the current loop character of input word and actual word
                    checkPresense = "G"                             #if condition evaluates true, setting the correctness variable as 'G'
                    break                                           #coming out of the inner loop
                elif checkChar1 == checkChar2 and letter != letter1:  #checking the similarity and index position of the current loop character of input word and actual word
                    checkPresense = "Y"                             #if condition evaluates true, setting the correctness variable as 'Y'
                    break                                           #coming out of the inner loop
                elif checkChar1 != checkChar2 and letter1 == len(word)-1:  #checking the similarity of the current loop character of input word and actual word, and whether the loop has reached the end of the actual word
                    checkPresense = "B"                             #if condition evaluates true, setting the correctness variable as 'B'
                    break                                           #coming out of the inner loop
            print(checkPresense, end = " ")                         #printing the correctness variable
        print("\n")                                                 #moving to next line
        if guessWord.lower() == word.lower():                       #when the input word is same as the actual word
            print("You won")                                        #printing the user has won the game
            goForNextRound = True                                   #declaring that the user can go to the next level
            totalChance = 0                                         #declaring the total chance as 0 as the user has won and no longer need to continue this level
        else:                                                       #when the input and actual words are not the same
            goForNextRound = False                                  #declaring the user cannot go to the next level
        totalChance -= 1                                            #decreasing the total chance by 1
    if(goForNextRound == False):                                    #when all 5 chances used and the user did not got to go to the next level
        print("Try again next time")                                #priting the user has lost
        print("The actual word is ", word)                          #printng the actual word

wordsList = ["car", "bat", "gate", "four", "sweet", "night"]        #initializing a list of words
checkSize = 3                                                       #initializing the size of the word to 3 initially
goForNextRound = True                                               #initializing go for next level as true as the player is in the first level

while(checkSize <= 5 and goForNextRound == True):                   #till the size of word is 5 or less and the player can go to next level
    findWord = getWord(checkSize)                                   #calling getWord() to get a random word
    playGame(findWord)                                              #calling playGame() to start playing the game
    checkSize += 1                                                  #increasing the size of the word


"""
test case 1
Enter a word : mad
B G B 

Enter a word : sad
B G B 

Enter a word : cad
G G B 

Enter a word : cat
G G B 

Enter a word : car
G G G 

You won
Enter a word : fly
Enter a 4 letter word : Four
G G G G 

You won
Enter a word : see
Enter a 5 letter word : Swing
G G B B B 

Enter a word : Sword
G G B B B 

Enter a word : Swarn
G G B B B 

Enter a word : Sweat
G G G B G 

Enter a word : Sweet
G G G Y G 

You won
____________________________

test case 2
Enter a word : smart
Enter a 3 letter word : see
B B B 

Enter a word : bag
G G B 

Enter a word : bar
G G B 

Enter a word : ban
G G B 

Enter a word : bae
G G B 

Try again next time
The actual word is  bat
__________________________________

"""