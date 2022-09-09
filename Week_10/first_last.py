def betweenLetters(word, letter):
    firstLetter = -1
    lastLetter = -1
    foundLetter = False
    firstLetter = word.find(letter)
    lastLetter = word.rfind("A")
    if(firstLetter ==-1 or firstLetter == lastLetter):
        print("There is no first A or last A")
    elif(firstLetter == lastLetter-1):
        print("There is no letter between first and last A")
        foundLetter = True
    else:
        print("Letters between first and last A")
        for letter in range(firstLetter+1, lastLetter):
            print(word[letter], end = " ")
        foundLetter = True
    return foundLetter

inputWord = input("Enter a word : ")
if(betweenLetters(inputWord, "A") == False):
    if(betweenLetters(inputWord, "B") == False):
        betweenLetters(inputWord, "C")



"""
test case 1
Enter a word : HELLO
There is no first A or last A
There is no first B or last B
There is no first C or last C
_______________________________
test case 2
Enter a word : AABB
There is no letter between first and last A
_______________________________
test case 3
Enter a word : AMAZINGSPACESHIP
Letters between first and last A
M A Z I N G S P
_______________________________
test case 4
Enter a word : APPLE
There is no first A or last A
There is no first B or last B
There is no first C or last C
_______________________________
test case 5
Enter a word : BABBLE BOY 
There is no first A or last A
Letters between first and last B
A B B L E
_______________________________
test case 6
Enter a word : ABBD
There is no first A or last A
There is no letter between first and last B
_______________________________
test case 7
Enter a word : RACING VEHICLES
There is no first A or last A
There is no first B or last B
Letters between first and last C
I N G   V E H I
_______________________________
test case 8
Enter a word : ACCB
There is no first A or last A
There is no first B or last B
There is no letter between first and last C
"""