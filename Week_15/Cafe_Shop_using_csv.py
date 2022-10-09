import csv
import pandas as pd

def openShop():
    shopStatus = input("Ready to take order or close the shop? Yes for open / No for close : ")
    if(shopStatus == "No"):
        exit()
    else:
        global noOrder
        noOrder = False
        takeOrder = True
        return takeOrder
def proceedRestock(orderedItems):
    supplyIndex = 2
    currentSupplyIndex = 3
    limitToRestockIndex = 6
    restockIndex = 0
    for info in itemsInfoList:
        info[currentSupplyIndex] -= orderedItems[restockIndex]
        supplyLimitToMaintain = info[supplyIndex] * (info[limitToRestockIndex] / 100)
        if info[currentSupplyIndex] <= supplyLimitToMaintain:
            info[currentSupplyIndex] = info[supplyIndex] - info[currentSupplyIndex]
            restockTimes[restockIndex] += 1
            restockIndex += 1

def readInputData():
    shopInputData = open(r"C:\Users\user\Desktop\Sayur Learning\Sowmiya\Week_15\input.csv", mode = "r")
    shopDataReader = csv.reader(shopInputData)
    next(shopDataReader)
    noOfItems = 0
    for data in shopDataReader:
        itemsInfoList.append([])
        for item in data:
            if item.isnumeric():
                item = int(item)
            itemsInfoList[noOfItems].append(item)
        noOfItems += 1

def createShopOutputData(itemsList):
    shopOutputData = open(r"C:\Users\user\Desktop\Sayur Learning\Sowmiya\Week_15\ouput.csv", mode = "w", newline = '')
    headerList = [["Items", "Items sold", "Restock times", "Sales", "Profit", "Balance stock"]]
    index = 1
    for items in itemsList:
        headerList.append([])
        headerList[index].append(items[0])
        for number in range(1,6):
            headerList[index].append(int(0))
        index += 1
    shopOutputDataWriter = csv.writer(shopOutputData)
    shopOutputDataWriter.writerows(headerList)
    shopOutputData.close()

def displayMenu(itemsList):
    menuItems = 1
    for item in itemsList:
        print(menuItems, item[0], "Rs.", item[1])
        menuItems += 1
    
def getOrder():
    itemIndex = 0
    currentSupplyIndex = 3
    orders = []
    for info in itemsInfoList:
        print("Attendent: How much of ", info[itemIndex], " do you want?")
        noOfItem = int(input("Customer : "))
        if noOfItem <= info[currentSupplyIndex]:
            orders.append(noOfItem)
        else:
            print("We have only ", info[currentSupplyIndex], " of ", info[itemIndex], ". How much do you want of them? ")
            noOfItem = int(input("Customer : "))
            orders.append(noOfItem)
    return orders

def readShopData():
    shopOutputData = open(r"C:\Users\user\Desktop\Sayur Learning\Sowmiya\Week_15\ouput.csv", mode = "r")
    next(shopOutputData)
    csvReader = csv.reader(shopOutputData)
    for data in csvReader:
        itemsSold.append(int(data[1]))
        restockTimes.append(int(data[2]))
        sales.append(int(data[3]))
        profit.append(int(data[4]))
        balanceStock.append(int(data[5]))
    shopOutputData.close()

def updateShopData(orderedItems):
    df = pd.read_csv(r"C:\Users\user\Desktop\Sayur Learning\Sowmiya\Week_15\ouput.csv")
    for i in range(len(orderedItems)):
        itemsSold[i] = itemsSold[i] + orderedItems[i]
        tempSale = orderedItems[i] * itemsInfoList[i][1]
        sales[i] = sales[i] + tempSale
        tempProfit = orderedItems[i] * itemsInfoList[i][6]
        profit[i] = profit[i] + tempProfit
        tempBal = itemsInfoList[i][3]
        balanceStock[i] = tempBal
    df["Items sold"] = itemsSold
    df["Restock times"] = restockTimes
    df["Sales"] = sales
    df["Profit"] = profit
    df["Balance stock"] = balanceStock
    df.to_csv(r"C:\Users\user\Desktop\Sayur Learning\Sowmiya\Week_15\ouput.csv", index = False)
    print(df)

noOrder = True
itemsInfoList = []
itemsSold = []
restockTimes = []
sales = []
profit = []
balanceStock = []
openToOrder = openShop()
if openToOrder == True and noOrder == False:
    readInputData()
    createShopOutputData(itemsInfoList)
    readShopData()

while(openToOrder == True):
    displayMenu(itemsInfoList)
    itemsOrdered = getOrder()
    proceedRestock(itemsOrdered)
    print(itemsSold, restockTimes, sales, profit, balanceStock)
    updateShopData(itemsOrdered)
    openShop()