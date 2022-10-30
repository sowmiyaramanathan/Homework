itemsList = []

def getSize():
    noOfItems = int(input("Enter number of items : "))
    return noOfItems

def getElements(noOfItems):
    for item in range(noOfItems):
        inputItem = int(input("Enter a number : "))
        itemsList.append(inputItem)

def sortInAscending(noOfItems):
    for item in range(0, noOfItems - 1):
        for item1 in range(0, noOfItems - 1 - item):
            if itemsList[item1] > itemsList[item1 + 1]:
                temp = itemsList[item1]
                itemsList[item1] = itemsList[item1 + 1]
                itemsList[item1 + 1] = temp
    print("Ascending Order : ", itemsList)

def sortInDescending(noOfItems):
    for item in range(0, noOfItems - 1):
        for item1 in range(0, noOfItems - 1 - item):
            if itemsList[item1] < itemsList[item1 + 1]:
                temp = itemsList[item1]
                itemsList[item1] = itemsList[item1 + 1]
                itemsList[item1 + 1] = temp
    print("Descending Order : ", itemsList)

sizeOfList = getSize()
getElements(sizeOfList)
sortInAscending(sizeOfList)
sortInDescending(sizeOfList)



"""
test case 1
Enter number of items : 5
Enter a number : 4
Enter a number : 8
Enter a number : 3
Enter a number : 2
Enter a number : 7
Ascending Order :  [2, 3, 4, 7, 8]
Descending Order :  [8, 7, 4, 3, 2]
"""