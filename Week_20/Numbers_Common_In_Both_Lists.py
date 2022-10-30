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
    return numList

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
findElementsInCommon(numbersListOne, numbersListTwo)
if len(commonElements) == 0:
    print("There is no common elements in the lists")
else:
    print("Numbers common in both the lists : ", *commonElements)



"""
test case 1
Enter the size of the two lists : 5
Enter the numbers in list 1  in ascending order : 
Enter element 1 1
Enter element 2 3
Enter element 3 7
Enter element 4 2
Enter element 5 4
Enter the numbers in list 2  in ascending order : 
Enter element 1 9
Enter element 2 2
Enter element 3 4
Enter element 4 3
Enter element 5 6
Numbers common in both the lists :  3 2 4
___________________________________________________________

test case 2
Enter the size of the two lists : 2
Enter the numbers in list 1  in ascending order : 
Enter element 1 1
Enter element 2 4
Enter the numbers in list 2  in ascending order : 
Enter element 1 5
Enter element 2 9
There is no common elements in the lists
___________________________________________________________
"""