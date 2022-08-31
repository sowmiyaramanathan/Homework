print("INSTRUCTIONS")               #printing the instructions for username and password
print("\nUsername:")
print("1. Username should contain @\n2. Username should contain any one of the following: .com, .edu. .tech, or .org")
print("\nPassword")
print("Password is the first, third and last three letters of your username followed by first three letters of the name of the company mentioned in the username and it should be followed by any three numbers") 

domain = [".com", ".edu", ".tech", ".org"]        #initializing acceptable domain names
username = input("Enter the username : ")           #reading username
enter_password = False                              #initializing boolean value whether to let the user enter password

if(username[0].isalpha()):                          #checking if the first letter of the username is a character(alphabet)
    check_for_at = "@" in username                  #checking whether the '@' symbol is present in the username
    if(check_for_at):
        check = username[-4::+1]                    #separating the domain name from the username
        if check in domain:                         #checking whether the domain is acceptable or not
            if(username[-5] == "@"):                #checking whether the '@' is present just before the domain name
                print("Invlaid username. '@' should be followed by characters.")
            else:
                print("Username is correct")            #if '@' is followed by alphabets printing username is correct
                enter_password = True                   #changing the boolean value to allow the user to enter the password
        else:
            print("Invalid username. Read instructions and try again")  #if domain is non acceptable ot not present, printing invalid username
    else:
        print("Invalid username. Read instructions and try again")      #if '@' is not present, printing invalid username
else:
    print("Username should start with an alphabet")                     #if username does not begin with alphabet, printing invaid username

if enter_password == True:                          #checking whether the boolen is set to allow the user to enter the password
    password = input("Enter your password : ")      #reading password from the user
    if(password[0] == username[0]):                 #checking whether the first letter of the username and the password is the same
        if(password[1] == username[2]):             #checking whether the second letter of password is same as the third letter of the username
            index_to_check = None                   #initializing a variable to get the index of '@' in username
            for index in range(len(username)):      #iteraing through the username
                if username[index] == '@':          #checking whether the current character is '@'
                    index_to_check = index          #assiging the current index in the index variable
                    break                           #using break as we have found the index of '@'
            three_username = username[index_to_check-3:index_to_check:+1]       #getting three characters before '@' in the username
            check_three_user = password[2:5]                               #getting three characters from third to fifth index of the password
            if(three_username == check_three_user):                             #checking whether those characters are the same
                three_comp = username[index_to_check+1:index_to_check+4:1]      #getting three characters after '@' in the username
                check_three_comp = password[5:8]                           #getting three characters from sixth to eighth index of the password
                if(three_comp == check_three_comp):                             #checking whether those characters are the same
                    last_three = password[8:11]                          #getting three characters from ninth to eleventh index of the password
                    if(last_three.isnumeric()):                                 #checking whether those charactes are numbers
                        print("Password is correct")                            #printing password is correct
                    else:
                        print("Invalid password. Read instructions and try again")      #if last three characters are not numeric, print invalid password
                else:
                    print("Invalid password. Read instructions and try again")      #if the comparison of the respective index charecters are not the same, print invalid password
            else:
                print("Invalid password. Read instructions and try again")      ##if the comparison of the respective index charecters are not the same, print invalid password
        else:
            print("Invalid password. Read instructions and try again")      #if the second letter of password and the third letter of the username are not the same, print invalid password
    else:
        print("Invalid password. Read instructions and try again")      #if the first letter of the username and the password are not the same, print invalid password



"""
test case 1
INSTRUCTIONS

Username:
1. Username should contain @
2. Username should contain any one of the following: .com, .edu. .tech, or .org

Password
Password is the first, third and last three letters of your username followed by first three letters of the name of the company mentioned in the username and it should be followed by any three numbers
Enter the username : Sowmiya@sayur.com
Username is correct
Enter your password : Swiyasay123
Password is correct

test case 2
INSTRUCTIONS

Username:
1. Username should contain @
2. Username should contain any one of the following: .com, .edu. .tech, or .org

Password
Password is the first, third and last three letters of your username followed by first three letters of the name of the company mentioned in the username and it should be followed by any three numbers
Enter the username : Sowmiya
Invalid username. Read instructions and try again

test case 3
INSTRUCTIONS

Username:
1. Username should contain @
2. Username should contain any one of the following: .com, .edu. .tech, or .org

Password
Password is the first, third and last three letters of your username followed by first three letters of the name of the company mentioned in the username and it should be followed by any three numbers
Enter the username : Sowmiya@.com
Invlaid username. '@' should be followed by characters.

test case 4
INSTRUCTIONS

Username:
1. Username should contain @
2. Username should contain any one of the following: .com, .edu. .tech, or .org

Password
Password is the first, third and last three letters of your username followed by first three letters of the name of the company mentioned in the username and it should be followed by any three numbers
Enter the username : Sowmiya@sayur.com
Username is correct
Enter your password : Swiyasay12s
Invalid password. Read instructions and try again

test case 5
INSTRUCTIONS

Username:
1. Username should contain @
2. Username should contain any one of the following: .com, .edu. .tech, or .org

Password
Password is the first, third and last three letters of your username followed by first three letters of the name of the company mentioned in the username and it should be followed by any three numbers
Enter the username : @sayur.com
Username should start with an alphabet
"""