import csv                          #importing CSV to perform read and write on CSV files
import pandas as pd                 #importing pandas with name as pd to write specific columns in a CSV

def openShop():                     #function to ask whether the shop is open to get orders
    shopStatus = input("Ready to take order or close the shop? Yes for open / No for close : ") #reading input from attender
    if(shopStatus == "No"):         #when response if no
        exit()                      #closing the shop
    else:                           #otherwise        
        takeOrder = True            #variable to indicate that the shop is open to take orders
        return takeOrder            #returning the takeOrder variable

def proceedRestock(orderedItems):       #function to perform restocking
    supplyIndex = 2                     #initializing the supply index
    currentSupplyIndex = 3              #initializing the current supply index
    limitToRestockIndex = 6             #initializing the restock limit index
    restockIndex = 0                    #variable to track the restocking count for the items accordingly
    for info in itemsInfoList:          #for loop to iterate all the items with their input data
        info[currentSupplyIndex] -= orderedItems[restockIndex]     #updating the current supply after customer's order
        supplyLimitToMaintain = info[supplyIndex] * (info[limitToRestockIndex] / 100)   #calculating the supply limit to maintain by referring the restock limit set in the input file
        if info[currentSupplyIndex] <= supplyLimitToMaintain:       #when the current supply is or goes below the supply to maintain
            info[currentSupplyIndex] = info[supplyIndex] - info[currentSupplyIndex] #increasing the current supply by the total number of items sold from the initial supply
            restockTimes[restockIndex] += 1                 #increasing the restock count by 1
            restockIndex += 1                               #increasing the tracking variable to track for the next item

def readInputData():                            #function to read and store the input data locally in the application
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

firstOrder = True             #setting the firstOrder variable to true as the shop data files are prepared for the first time when the first customer arrives until then, the files are not accessed
itemsInfoList = []
itemsSold = []
restockTimes = []
sales = []
profit = []
balanceStock = []
openToOrder = openShop()
if openToOrder == True and firstOrder == True:
    readInputData()
    createShopOutputData(itemsInfoList)
    readShopData()

while(openToOrder == True):
    displayMenu(itemsInfoList)
    itemsOrdered = getOrder()
    proceedRestock(itemsOrdered)
    updateShopData(itemsOrdered)
    openShop()