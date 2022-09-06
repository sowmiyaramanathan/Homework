def betweenABC(word):
    first_A = -1
    last_A = -1
    first_B = -1
    last_B = -1
    first_C = -1
    last_C = -1

    first_A = word.find("A")
    first_B = word.find("B")
    first_C = word.find("C")
    last_A = word.rfind("A")
    last_B = word.rfind("B")
    last_C = word.rfind("C")
    
    if(first_A==-1 or first_A == last_A):
        print("There is no first A or last A")
        if(first_B==-1 or first_B == last_B):
            print("There is no first B or last B")
            if(first_C==-1 or first_C == last_C):
                print("There is no first C or last C")
            elif(first_C == last_C-1):
                print("There is no letter between first and last C")
            else:
                print("Letters between first and last C")
                for letter in range(first_C+1, last_C):
                    print(word[letter], end = " ")
        elif(first_B == last_B-1):
            print("There is no letter between first and last B")
        else:
            print("Letters between first and last B")
            for letter in range(first_B+1, last_B):
                print(word[letter], end = " ")
    elif(first_A == last_A - 1):
        print("There is no letter between first and last A")
    else:
        print("Letters between first and last A")
        for letter in range(first_A+1, last_A):
            print(word[letter], end = " ")
        
word = input("Enter a word: ")
betweenABC(word)


"""
test case 1
Enter a word: HELLO
There is no first A or last A
There is no first B or last B
There is no first C or last C
_________________________________
test case 2
Enter a word: AABB
There is no letter between first and last A
_________________________________
test case 3
Enter a word : AMAZINGSPACEJET
Letters between first and last A
M A Z I N G S P
_________________________________
test case 4
Enter a word : APPLE
There is no first A or last A
There is no first B or last B
There is no first C or last C
_________________________________
test case 5
Enter a word: BABBLE BOY
There is no first A or last A
Letters between first and last B
A B B L E
_________________________________
test case 6
Enter a word: ABBD
There is no first A or last A
There is no letter between first and last B
_________________________________
test case 7
Enter a word : RACING VEHICLES
There is no first A or last A
There is no first B or last B
Letters between first and last C
I N G   V E H I
_________________________________
test case 8
Enter a word : ACCB
There is no first A or last A
There is no first B or last B
There is no letter between first and last C
"""