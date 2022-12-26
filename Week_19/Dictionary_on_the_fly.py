itemsData = {
    "Sandwich" : {
        "Price" : 40,
        "Supply" : 100,
        "Sales" : 0
    },
    "Donut" : {
        "Price" : 50,
        "Supply" : 100,
        "Sales" : 0
    },
    "Coke" : {
        "Price" : 30,
        "Supply" : 100,
        "Sales" : 0
    }
}
maxTransaction = 10
openToOrder = 'yes'

salesDict = {}
keysForSalesDict = list(itemsData)

for item in itemsData.keys():
    print(item, " - Rs.", itemsData[item]["Price"])
    
while maxTransaction > 0 and openToOrder == "yes":
    for item in itemsData.keys():
        noOfItem = int(input("How much " + item + " do you want? "))
        if noOfItem <= itemsData[item]["Supply"]:
            salesDict[keysForSalesDict[0]] = {"Sales" , "Supply"}
            print(type(salesDict))
            print(salesDict)
            
            salesDict[keysForSalesDict[0]]['Sales'].append(0)
            # salesDict[keysForSalesDict[0]][1] -= noOfItem
            # salesDict[keysForSalesDict[0]][0] += noOfItem * itemsData[item]["Price"]
            # print(salesDict)
        else:
            print("Out of stock")
    maxTransaction -= 1
    openToOrder = input("Open to receive orders (yes / no) : ")

for item in itemsData.keys():
    print("Sales in ", item, " - ", itemsData[item]["Sales"])