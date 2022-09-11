import re
domainNames = [".com", ".edu", ".tech", ".org"]
userName = input("Enter the username : ")   
foundUserName = False

if(len(userName) >= 10):
    if userName.__contains__("@"):
        for domain in range(len(domainNames)):
            domainToBeIn = domainNames[domain]
            checkForUserName = r"[a-zA-Z0-9]+@[a-zA-Z0-9]+" + domainToBeIn
            if re.search(checkForUserName, userName):
                foundUserName = True
        if(foundUserName == True):
            print("Username accepted")    
        else:
            print("Enter valid username")
    else:
        print("Username should contain '@'")
else:
    print("The username must contain atleast 10 characters")


if(foundUserName == True):
    passWord = input("Enter password: ")
    foundPassWord = False
    firstString = userName[0]
    secondString = userName[2]
    checkForAt = userName.index("@")
    thirdString = userName[checkForAt-3:checkForAt:+1]
    fourthString = userName[checkForAt+1:checkForAt+4:+1]
    fullString = firstString + secondString + thirdString + fourthString
    # if re.search(rf"{fullString}" + r"[0-9]+", passWord):
    #     print("Done")
    # # # passWordAccepted = checkForPassword.match(passWord)
    # if(foundPassWord == True):
    #     print("Password Accepted")
    # else:
    #     print("Enter valid password")