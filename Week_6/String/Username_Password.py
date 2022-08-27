print("INSTRUCTIONS")
print("\nUsername:")
print("1. Username should contain @\n2. Username should contain any one of the following: .com, .edu. .tech, or .org")
print("\nPassword")
print("Password is the first, third and last three letters of your username followed by first three letters of the name of the company mentioned in the username and it should be followed by any three numbers") 

word = [".com", ".edu", ".tech", ".org"]
username = input("Enter the username : ")
enter_password = False

check_for_at = "@" in username
if(check_for_at):
    check = username[-4::+1]
    if check in word:
        if(username[-5] == "@"):
            print("Invlaid username. '@' should be followed by characters.")
        else:
            print("Username is correct")
            enter_password = True
    else:
        print("Invalid username. Read instructions and try again")
else:
    print("Invalid username. Read instructions and try again")

if enter_password == True:
    password = input("Enter your password : ")
    if(password[0] == username[0]):
        if(password[1] == username[2]):
            index_to_check = 0
            for index in range(len(username)):
                if username[index] == '@':
                    index_to_check = index
                    break
            three_username = username[index_to_check-3:index_to_check:+1]
            check_three_user = password[2:5]
            if(three_username == check_three_user):
                three_comp = username[index_to_check+1:index_to_check+4:1]
                check_three_comp = password[5:8]
                if(three_comp == check_three_comp):
                    last_three = password[8:11]
                    if(last_three.isnumeric()):
                        print("Password is correct")
                    else:
                        print("Invalid password. Read instructions and try again")
                else:
                    print("Invalid password. Read instructions and try again")
            else:
                print("Invalid password. Read instructions and try again")
        else:
            print("Invalid password. Read instructions and try again")
    else:
        print("Invalid password. Read instructions and try again")   



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
"""