import string
password = input("Enter your password : ")
count_alpha = 0
count_num = 0
count_spec = 0

if(password.isalpha() or password.isnumeric() or (all(i in string.punctuation for i in password))):
    print("Password is weak. Not acceptable")
else:
    for char in password:
        if char.isalpha():
            count_alpha += 1
        if char.isnumeric():
            count_num += 1
        if char in string.punctuation:
             for char in password:
                count_spec += 1
    if(count_alpha >= 1 and count_num >= 1 and count_spec >= 1):
        if(count_alpha >= 3 and count_num >= 2 and count_spec >= 1):
            if(len(password) >= 16):
                print("Very Strong. Password accepted")
            else:
                print("Strong. Password accepted")
        else:
            print("OK. Password accepted")



"""
test case 1
Enter your password : School
Password is weak. Not acceptable

test case 2
Enter your password : 20041999
Password is weak. Not acceptable

test case 3
Enter your password : #$@%^
Password is weak. Not acceptable

test case 4
Enter your password : School@001
Strong. Password accepted

test case 5
Enter your password : S@#34
OK. Password accepted

test case 6
Enter your password : Horizonhigh@67321
Very Strong. Password accepted

test case 6
Enter your password : Sowmi2@
OK. Password accepted
"""