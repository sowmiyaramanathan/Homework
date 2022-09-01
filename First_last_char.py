word = input("Enter a word : ")     #reading input

start = 0                           #intiailizing start index
stop = len(word)//2                 #intializing stop index

for letter in range(len(word)-1, stop-1, -1):           #iterating the word till stop value in reverse
    print(word[start], end = "")                        #printing the start index element
    print(word[letter], end = "")                       #printing the stop index element
    start += 1                                          #increasing start count by 1
    if(len(word)%2 == 0):             #checking the length of the word to check if we have printed all the elements
        if(start == stop):                              #checking if we reached the end i.e., printed all elements
            break                                       #using break to stop the execution
    else:                                               #using else in case of odd length
        if(start == stop):                              #checking if we reached the end i.e., one element is left
            print(",", end = "")    #printing a comma as we cannot print the comma that is after this block i.e.., we are going to break the loop in this block
            print(word[start])                          #printing the single element that has been left
            break                                       #using break to stop the execution
    print(",", end = "")                                #printing a comma



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