myList = [1,2,3,4,5,6,7,8,9,10]

def max_list(myList):
    max = myList[0]
    for i in range(1, len(myList)):
        if max <= myList[i]:
            max = myList[i]
    return max

result = max_list(myList)
print(result)