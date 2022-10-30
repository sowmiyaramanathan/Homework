import re

def askUser():
    print("Select\n1 to Encode a message\n2 to Decode a message")
    userChoice = int(input("Enter your choice : "))
    return userChoice

def getMessage():
    userInputMessage = input("Enter message to encode : ")
    toEncode = userInputMessage.split(' ')
    return toEncode

def getCode():
    userInputCode = input("Enter code to decode")
    toDecode = userInputCode.split(' ')
    return toDecode

def checkMessage(message):
    checkForNumber = r"[0-9]"
    for char in message:
        if char[len(char) - 1] in vowels:
            vowelInLast(char)
        elif re.search(checkForNumber, char):
            numberInFirst(char)
        else:
            normalWord(char)

def vowelInLast(message):
    codedMessage = ""
    firstLetterInCodedMessage = message[-1]
    message = message.replace(firstLetterInCodedMessage, ' ')
    codedMessage += firstLetterInCodedMessage
    codedMessage += message
    print(codedMessage, end = " ")

def numberInFirst(message):
    codedMessage = ""
    messageTransformation = numbers[message]
    codedMessage += "A" + messageTransformation + "A"
    print(codedMessage, end = " ")

def normalWord(message):
    codedMessage = ""
    messageSize = len(message) // 2
    if messageSize % 2 == 0:
        firstHalfPattern = message[messageSize + 1  : ]
        secondHalfPattern = message[ : messageSize]
        middlePattern = message[messageSize]
        codedMessage += firstHalfPattern + middlePattern + secondHalfPattern
    else:
        firstHalfPattern = message[messageSize : ]
        secondHalfPattern = message[ : messageSize]
        codedMessage += firstHalfPattern + secondHalfPattern
    print(codedMessage, end = " ")


vowels = ['a', 'e', 'i', 'o', 'u']
numbers = { '0' : 'one', '1' : 'one', '2':'two', '3' : 'three', '4' : 'four', '5' : 'five', '6' : 'six', '7' : 'seven', '8' : 'eight', '9' : 'nine', '10' : 'ten', '11' : 'eleven', '12' : 'twelve'}
userChoice = askUser()
if userChoice == 1:
    userMessage = getMessage()
    checkMessage(userMessage)
if userChoice == 2:
    userCode = getCode()
    # checkCode(userCode)



"""
test case 1 - Encoding a message
Select
1 to Encode a message
2 to Decode a message
Enter your choice : 1
Enter message to encode : meet me at the river at 7 pm today
teme em  ta eth  ervri ta AsevenA mp aydto 

"""