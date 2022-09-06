def betweenA(word):
    first_A = -1
    last_A = -1
    first_A = word.find("A")
    last_A = word.rfind("A")
    if(first_A==-1 or first_A == last_A):
        print("There is no first A or last A")
        betweenB(word)
    elif(first_A == last_A-1):
        print("There is no letter between first and last A")
    else:
        print("Letters between first and last A")
        for letter in range(first_A+1, last_A):
            print(word[letter], end = " ")

def betweenB(word):
    first_B = -1
    last_B = -1
    first_B = word.find("B")
    last_B = word.rfind("B")
    if(first_B==-1 or first_B == last_B):
        print("There is no first B or last B")
        betweenC(word)
    elif(first_B == last_B-1):
        print("There is no letter between first and last B")
    else:
        print("Letters between first and last B")
        for letter in range(first_B+1, last_B):
            print(word[letter], end = " ")

def betweenC(word):
    first_C = -1
    last_C = -1
    first_C = word.find("C")
    last_C = word.rfind("C")
    if(first_C==-1 or first_C == last_C):
        print("There is no first C or last C")
    elif(first_C == last_C-1):
        print("There is no letter between first and last C")
    else:
        print("Letters between first and last C")
        for letter in range(first_C+1, last_C):
            print(word[letter], end = " ")

word = input("Enter a word : ")
betweenA(word)


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