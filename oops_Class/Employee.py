class Employee():
    def __init__(self):
        self.empName = ''
        self.empID = ''
        self.empDept = ''
        self.empManager = None

    def getManagerHierarchy(self):
        while self.empManager is not None:
            print(self.empName + "'s manager is " + self.empManager.empName)
            self = self.empManager
        else:
            print(self.empName + " has no manager")

peter = Employee()
peter.empName = 'Peter'
peter.empID = '1'
peter.empDept = 'Software'

harry = Employee()
harry.empName = 'Harry'
harry.empID = '2'
harry.empDept = 'Software'
harry.empManager = peter

olivia = Employee()
olivia.empName = 'Olivia'
olivia.empID = '3'
olivia.empDept = 'Software'
olivia.empManager = harry

steve = Employee()
steve.empName = 'Steve'
steve.empID = '4'
steve.empDept = 'Software'
steve.empManager = olivia

sam = Employee()
sam.empName = 'Sam'
sam.empID = '5'
sam.empDept = 'Software'

lisa = Employee()
lisa.empName = 'Lisa'
lisa.empID = '6'
lisa.empDept = 'Software'
lisa.empManager = sam

employees = [peter, harry, olivia, steve, sam, lisa]
userInput = input("Enter employee ID : ")

flag = ""
for employee in employees:
    if employee.empID == userInput:
        print(employee.empName + "'s ID is " + userInput)
        employee.getManagerHierarchy()
        flag = None
        break

if flag is not None:
    print("Wrong employee ID entered")