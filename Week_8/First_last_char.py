word = input("Enter a word : ")     #reading input

firstHalf = len(word)//2            #initializing first half
secondHalf = len(word) - 1          #initializing second half

for letter in range(0, firstHalf):                          #iterating the firsthalf
    print(word[letter], end = "" + word[secondHalf])        #printing firsthalf and secondhalf elements
    if(firstHalf == secondHalf):                            #checking if both the indexes are the same
        break                                               #breaking from the statement
    print(",", end ="")                                     #printing comma
    secondHalf -= 1                                         #decreasing secondhalf index by 1
if(len(word)%2 != 0):                                       #checking the length of the word
    print(word[firstHalf])                                  #in case of odd, printing the left out element



"""
test case 1
Enter a word : ABCD1234
A4,B3,C2,D1

test case 2
Enter a word : abc12
a2,b1,c

test case 3
Enter a word : mahesh2000
m0,a0,h0,e2,sh

test case 4
Enter a word : apple23
a3,p2,pe,l
"""