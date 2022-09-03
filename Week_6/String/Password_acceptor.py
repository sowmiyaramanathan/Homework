import string
password = input("Enter your password : ")      #reading input from the user
count_alpha = 0                                 #initialzing a variable to store the count of alphabets
count_num = 0                                   #initialzing a variable to store the count of numbers
count_spec = 0                                 #initialzing a variable to store the count of special character
password_length = len(password)

if(password_length>=8):
    if(password.isalpha() or password.isnumeric() or (all(i in string.punctuation for i in password))): #checking whether the input contains only alphabets or numbers or special characters
        print("Password is weak. Not acceptable")       #printing password is weak
    else:                               #using else to check further
        for char in password:           #iterating through the input word
            if char.isalpha():          #checking if the current character in the input is an alphabet
                count_alpha += 1        #increasing the alphabet count by 1
            if char.isnumeric():        #checking if the current character in the input is a number
                count_num += 1          #increasing the number count by 1
            if char in string.punctuation:  #checking if the current character in the input is a special character
                count_spec += 1         #increasing the special character count by 1
        if(count_alpha >= 1 and count_num >= 1 and count_spec >= 1):        #checking whether the count of all characters is atleast 1
            if(count_alpha >= 3 and count_num >= 2 and count_spec >= 1):    #checking the count of characters
                max_length = 16                 #initializing the maximum length of the password as 16
                if(password_length >= max_length):                             #checking the length of the word
                    print("Very Strong. Password accepted")         #printing password is very strong
                else:
                    print("Strong. Password accepted")              #printing password is strong
            else:
                print("OK. Password accepted")                      #printing password is ok
else:
    print("Invalid. The password should contain minmum 8 characters")



"""
test case 1
Enter your password : School
Invalid. The password should contain minmum 8 characters

test case 2
Enter your password : 20041999
Password is weak. Not acceptable

test case 3
Enter your password : #$@%#@%$%
Password is weak. Not acceptable

test case 4
Enter your password : School@001
Strong. Password accepted

test case 5
Enter your password : S@#454@@
OK. Password accepted

test case 6
Enter your password : Horizonhigh@67321
Very Strong. Password accepted

test case 6
Enter your password : Sowmi2@
OK. Password accepted
"""