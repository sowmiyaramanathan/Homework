numbersListOne = []
numbersListTwo = []
commonElements = []

def getListSize():
    listSize = int(input("Enter the size of the two lists : "))
    return listSize

def getElements(noOfItems, numList, number):
    print("Enter the numbers in list", number , " in ascending order : ")
    for number in range(noOfItems):
        item = int(input("Enter element " + str((number) + 1) + " "))
        numList.append(item)

def findElementsInCommon(listOne, listTwo):
    for num1 in listOne:
        if num1 in commonElements:
            break
        else:
            if num1 in listTwo:
                commonElements.append(num1)

listSize = getListSize()
numbersListOne = getElements(listSize, numbersListOne, "1")
numbersListTwo = getElements(listSize, numbersListTwo, "2")
findElementsInCommon([1,2,3], [2,3,4])
print(commonElements)