class Employee():
    def __init__(self):
        self.empName = ''
        self.empID = ''
        self.empDept = ''
        self.empManager = None

    def getManagerHierarchy(self):
        empObj = self
        while empObj.empManager is not None:
            print(empObj.empName + "'s manager is " + empObj.empManager.empName)
            empObj = empObj.empManager
        else:
            print(empObj.empName + " has no manager")

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



"""
test case 1
Enter employee ID : 5
Sam's ID is 5
Sam has no manager
____________________________________

test case 2
Enter employee ID : 6
Lisa's ID is 6
Lisa's manager is Sam
Sam has no manager
____________________________________

test case 3
Enter employee ID : 11
Wrong employee ID entered
____________________________________

test case 4
Enter employee ID : 4
Steve's ID is 4
Steve's manager is Olivia
Olivia's manager is Harry
Harry's manager is Peter
Peter has no manager
"""