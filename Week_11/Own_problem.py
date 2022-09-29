def getSalary():                        #function to get salary
    salary = int(input("Enter you monthly salary : "))  #reading salary
    if salary <= 0:
        print("Enter a valid amount")        #when salary is 0 or less, notifying the user
        exit()
    else:
        return salary                        #returning salary

def chooseMethod():                     #function to let the user select how he/she wants the budget plan
    userDecision = int(input("Type 1 for customized budget plan / 0 for deafult budget plan : "))               #reading default or customized plan
    if userDecision == 1:
        return 1                            #returning 1 in case of default plan
    elif userDecision == 0:
        return 0                            #returning 0 in case of customized plan
    else:
        print("Enter only 1 or 0")          #if the input is not 1 or 0, notifying the user
        exit()                              #exiting application

def idealBudget(salary):                    #function for default plan
    global needAmount, wantAmount, saveAmount
    needAmount = salary / 2                 #50% of salary
    wantAmount = (salary * 3) / 10          #30% of salary
    saveAmount = salary / 5                 #20% of salary
  
def getRequirements():                      #function to get expenses of needs
    listOfNeeds = ["monthly rent", "electricity and gass bills", "transportation", "insurance(health, vehicle, pets)", "minimum loan repayments", "groceries", "others"]        #list of essential needs
    for needs in range(len(listOfNeeds)):
        print("How much do you need for ", listOfNeeds[needs])      #reading amount of expense for each needs
        expenseOfNeeds.append(int(input()))         #adding the amount to the corresponding list

def customBudget(needs, salary):                #function for customized plan
    global needAmount, wantAmount, saveAmount   #declaring global variables
    needAmount = sum(needs)                     #calculating sum of the expenses of needs
    actualNeedAmount = salary // 2              #calculating the ideal need amount
    balSalary = salary - needAmount             #calculating the balance after the expenses of the needs
    wantAmount = (balSalary * 2) // 3           #calculating amount for wants
    saveAmount = balSalary - wantAmount         #calculating amount for savings
    if needAmount > actualNeedAmount:
        print("OOPS! You might have to tolerate in your wants and savings")
    elif needAmount == salary:
        print("Your whole salary has been used up by your needs")
    else:
        print("You are in safe zone")


def displaybudget():                #function to display the budget plan
    print("Your budget for this month is ")
    print("Amount for needs : Rs.", needAmount)
    print("Amount for wants : Rs.", wantAmount)
    print("Amount for savings : Rs.", saveAmount)

needAmount = None
wantAmount = None
saveAmount = None
expenseOfNeeds = []                     #list to store the expenses of needs
monthlySalary = getSalary()             #calling getSalary() to read monthly salary
methodprefered = chooseMethod()         #calling chooseMethod() to get the prefered plan

if(methodprefered == 1):            #using customized plan in case the prefered method is 1
    getRequirements()
    customBudget(expenseOfNeeds, monthlySalary)
    displaybudget()
else:                               #using default plan in case the prefered method is 0
    idealBudget(monthlySalary)
    displaybudget()


"""
test case 1 - default plan
Enter you monthly salary : 2000
Type 1 for customized budget plan / 0 for deafult budget plan : 0
Your budget for this month is 
Amount for needs : Rs. 1000.0
Amount for wants : Rs. 600.0
Amount for savings : Rs. 400.0
________________________________________________________

test case 2 - customized plan
Enter you monthly salary : 20000
Type 1 for customized budget plan / 0 for deafult budget plan : 1
How much do you need for  monthly rent
3000
How much do you need for  electricity and gass bills
1000
How much do you need for  transportation
1000
How much do you need for  insurance(health, vehicle, pets)
3000
How much do you need for  minimum loan repayments
2000
How much do you need for  groceries
2000
How much do you need for  others
3000
OOPS! You might have to tolerate in your wants and savings
Your budget for this month is
Amount for needs : Rs. 15000
Amount for wants : Rs. 3333
Amount for savings : Rs. 1667
________________________________________________________

test case 3 - salary value 0 or less
Enter you monthly salary : 0
Enter a valid amount
________________________________________________________

test case 4 - invalid method selection
Enter you monthly salary : 50000
Type 1 for customized budget plan / 0 for deafult budget plan : 5
Enter only 1 or 0
"""