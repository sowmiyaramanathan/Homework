import re

vowels = ['a', 'e', 'i', 'o', 'u']
numbers = { '0' : 'one', '1' : 'one', '2':'two', '3' : 'three', '4' : 'four', '5' : 'five', '6' : 'six', '7' : 'seven', '8' : 'eight', '9' : 'nine', '10' : 'ten', '11' : 'eleven', '12' : 'twelve'}
codedMessage = []
codedPatternTrack = []
decodedCode = []

def askUser():                                      # method to ask the user for choice
    print("Select\nPress 1 to Encode a message\nPress 2 to Decode a message")
    userChoice = int(input("Enter your choice : "))
    return userChoice

def getMessage():                                   # method to get message to encode it
    userInputMessage = input("Enter message to encode : ")
    toEncode = userInputMessage.split(' ')
    return toEncode

def getCode():                                      # method to get code to decode it
    userInputCode = input("Enter code to decode : ")
    toDecode = userInputCode.split(' ')
    return toDecode

def checkMessage(message):                          # method to check the message pattern to encode it
    checkForNumber = r"[0-9]"
    for word in message:
        if word[len(word) - 1] in vowels:
            codedPatternTrack.append(vowelInLast(word))
        elif re.search(checkForNumber, word):
            codedPatternTrack.append(numberInFirst(word))
        else:
            codedPatternTrack.append(normalWord(word))

def vowelInLast(message):                 # method to encode a message that contains a vowel at the end
    encodedMessage = ""
    firstLetterInCodedMessage = message[len(message) - 1]
    encodedMessage += firstLetterInCodedMessage + message[0 : len(message) - 1]
    codedMessage.append(encodedMessage)
    return 'vowelPattern'

def numberInFirst(message):                # method to encode a message that is a number
    encodedMessage = ""
    messageTransformation = numbers[message]
    encodedMessage += "A" + messageTransformation + "A"
    codedMessage.append(encodedMessage)
    return 'numberPattern'

def normalWord(message):          # method a encode a message that is not a number and ends with a consonant
    encodedMessage = ""
    messageSize = len(message) // 2
    if len(message) % 2 != 0:
        firstHalfPattern = message[messageSize + 1  : ]
        secondHalfPattern = message[ : messageSize]
        middlePattern = message[messageSize]
        encodedMessage += firstHalfPattern + middlePattern + secondHalfPattern
    else:
        firstHalfPattern = message[messageSize : ]
        secondHalfPattern = message[ : messageSize]
        encodedMessage += firstHalfPattern + secondHalfPattern
    codedMessage.append(encodedMessage)
    return 'normalPattern'

def checkCode(code):
    for word in range(len(code)):
        if codedPatternTrack[word] == 'vowelPattern':
            vowelInFirst(code[word])
        elif codedPatternTrack[word] == 'numberPattern':
            aInFirst(code[word])
        elif codedPatternTrack[word] == 'normalPattern':
            normalCode(code[word])

def vowelInFirst(code):
    deCodedMessage = ""
    lastLetterInDecodedMessage = code[:1]
    deCodedMessage += code[1 :] + lastLetterInDecodedMessage
    decodedCode.append(deCodedMessage)

def aInFirst(code):
    transformedCode = code[1 : len(code) - 1]
    deCodedMessage = { val for val in numbers if numbers[val] == transformedCode}
    deCodedMessage = ''.join(deCodedMessage)
    decodedCode.append(deCodedMessage)

def normalCode(code):
    deCodedMessage = ""
    codeSize = len(code) // 2
    if len(code) % 2 != 0:
        firstHalfPattern = code[codeSize + 1 : ]
        secondHalfPattern = code[: codeSize]
        middlePattern = code[codeSize]
        deCodedMessage += firstHalfPattern + middlePattern + secondHalfPattern
    else:
        firstHalfPattern = code[codeSize : ]
        secondHalfPattern = code[ : codeSize]
        deCodedMessage += firstHalfPattern + secondHalfPattern
    decodedCode.append(deCodedMessage)

userChoice = askUser()
if userChoice == 1:
    userMessage = getMessage()
    checkMessage(userMessage)
    print("Encoded Message : ", *codedMessage)
userChoice = askUser()
if userChoice == 2:
    userCode = getCode()
    checkCode(userCode)
    print("Decoded Message : ", *decodedCode)



"""
Select
Press 1 to Encode a message
Press 2 to Decode a messageEnter your choice : 1
Enter message to encode : meet me at the river at 7 pm today  
Encoded Message : etme em ta eth ervri ta AsevenA mp aydto
Select
Press 1 to Encode a message
Press 2 to Decode a message
Enter your choice : 2
Enter code to decode : etme em ta eth ervri ta AsevenA mp aydto
Decoded Message : meet me at the river at 7 pm today
"""