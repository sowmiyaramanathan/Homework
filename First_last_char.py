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
    print(",", end = "")