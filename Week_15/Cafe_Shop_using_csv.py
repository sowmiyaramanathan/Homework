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
    shopInputData = open(r"C:\Users\user\Desktop\Sayur Learning\Sowmiya\Week_15\input.csv", mode = "r") #opening the input file in read mode
    shopDataReader = csv.reader(shopInputData)          #initializing reader for the input file
    next(shopDataReader)                                #skipping the header row
    noOfItems = 0                                       #variable indicating the index of a list to add the list of items with their data
    for item in shopDataReader:                         #for loop to go through each rows in the input file
        itemsInfoList.append([])                        #creating a sublist into the itemInfoList to add individual items with their data
        for data in item:                               #for loop to go through data of individual items
            if data.isnumeric():                        #if the data is a numeric
                data = int(data)                        #storing the data as an integer 
            itemsInfoList[noOfItems].append(data)       #adding the data into the sublist
        noOfItems += 1                                  #increasing the variable indicating the index by 1 to store the next item

def createShopOutputData(itemsList):                    #function to create a output file for the shop that contains information of transactions done while the shop was open
    shopOutputData = open(r"C:\Users\user\Desktop\Sayur Learning\Sowmiya\Week_15\ouput.csv", mode = "w", newline = '')  #opening the output file in write to set the headers and initialize the output values to which the processed values are going to be updated
    initialValueList = [["Items", "Items sold", "Restock times", "Sales", "Profit", "Balance stock"]] #initializing a list with sublists containing information which are going to be written into the output file when the shop opens for the first time
    index = 1                                           #variable denoting the index of the list
    for items in itemsList:                             #for loop to go through the list of items with their data
        initialValueList.append([])                     #adding a sublist to the initialValueList
        initialValueList[index].append(items[0])        #in the sublist, adding the item name
        for number in range(1,6):                       #for loop to initialize values for the output file
            initialValueList[index].append(int(0))      #in the sublist, adding the initial values as 0
        index += 1                                      #increasing the index of the initialValueList
    shopOutputDataWriter = csv.writer(shopOutputData)   #initializing writer to write the initialized values to the output file
    shopOutputDataWriter.writerows(initialValueList)    #writing the contents in the initialValueList into the output file
    shopOutputData.close()                              #closing the output file

def readShopOutputData():                                     #function for reading the output file to retrieve the initial information present, so that we can process over it
    shopOutputData = open(r"C:\Users\user\Desktop\Sayur Learning\Sowmiya\Week_15\ouput.csv", mode = "r")    #opening the output file in reading mode
    next(shopOutputData)                                #skipping the header rows
    csvReader = csv.reader(shopOutputData)              #initializing reader to read the contents in the output file
    for data in csvReader:                              #for loop to go through each rows and adding the initial values present in the output file when the first opened for sometime to their respective lists
        itemsSold.append(int(data[1]))
        restockTimes.append(int(data[2]))
        sales.append(int(data[3]))
        profit.append(int(data[4]))
        balanceStock.append(int(data[5]))
    shopOutputData.close()                              #closing the output file

def displayMenu(itemsList):                             #function to display menu items to the customer
    menuItems = 1
    for item in itemsList:
        print(menuItems, item[0], "Rs.", item[1])
        menuItems += 1

def getOrder():                                         #function to get orders from the customer
    itemIndex = 0                                       #initializing item index
    currentSupplyIndex = 3                              #initialzing current supply index
    orders = []                                         #initializing orders list
    for info in itemsInfoList:                          #for each item in the itemInfoLits
        print("Attendent: How much of ", info[itemIndex], " do you want?")  #asking for the input
        noOfItem = int(input("Customer : "))                            #areading the input
        if noOfItem <= info[currentSupplyIndex]:                        #if the ordered number of items is less than or equal to the the supply present in the shop
            orders.append(noOfItem)                                     #adding the item to the orders list
        else:                                                           #if supply is less
            print("We have only ", info[currentSupplyIndex], " of ", info[itemIndex], ". How much do you want of them? ")                                                    #asking customer to revise the order
            noOfItem = int(input("Customer : "))                        #reading revised input
            orders.append(noOfItem)                                     #adding the reviders input to the orders list
    return orders                                                       #returning the orders list

def updateShopOutputData(orderedItems):                                       #function to update the outpu file
    outpuFile = pd.read_csv(r"C:\Users\user\Desktop\Sayur Learning\Sowmiya\Week_15\ouput.csv") #opening the output file as a dataframe using pandas
    for item in range(len(orderedItems)):                               #for loop to go throgh the ordered items
        itemsSold[item] += + orderedItems[item]          #adding the number of items ordered on a particular item to the value in the itemsSold list
        tempSale = orderedItems[item] * itemsInfoList[item][1]          #calculating the amount earned on an item for an order and storing it in a temporary sales variable
        sales[item] = sales[item] + tempSale                            #adding the sales variable to the value in the sales list
        tempProfit = orderedItems[item] * itemsInfoList[item][6]        #calculaing the profit earned on an item by refering the profit margin and storing it in a temporary profit variable
        profit[item] = profit[item] + tempProfit                        #adding the profit variable to the value in the profit list
        tempBal = itemsInfoList[item][3]                                #storing the current supply as temporary balance stack variable
        balanceStock[item] = tempBal                                    #assigning the temporary balance stock to the balance stock list
    #writing the updated information to the output file by refering the header row
    outpuFile["Items sold"] = itemsSold
    outpuFile["Restock times"] = restockTimes
    outpuFile["Sales"] = sales
    outpuFile["Profit"] = profit
    outpuFile["Balance stock"] = balanceStock
    outpuFile.to_csv(r"C:\Users\user\Desktop\Sayur Learning\Sowmiya\Week_15\ouput.csv", index = False)  #converting the output file to csv

firstOrder = True               #setting the firstOrder variable to true as the shop data files are prepared for the first time when the first customer arrives until then, the files are not accessed
itemsInfoList = []              #initializing required lists to store and update the output file data
itemsSold = []
restockTimes = []
sales = []
profit = []
balanceStock = []
openToOrder = openShop()                          #calling openShop() function to get whether the shop is open or not
if openToOrder == True and firstOrder == True:    #when the shop is open and it is the first order / customer
    readInputData()                             #calling readInputData() to read the input data and store them locally
    createShopOutputData(itemsInfoList)         #calling createShopOutputData() to create an output file and initialize values in the file
    readShopOutputData()                        #calling readShopOutputData() to read and store the initialized values locally

while(openToOrder == True):                 #till the shop is open
    displayMenu(itemsInfoList)              #calling displayMenu() to display menu
    itemsOrdered = getOrder()               #calling getOrder() to get orders
    proceedRestock(itemsOrdered)            #calling proceedRestock() to check whether to restock or not
    updateShopOutputData(itemsOrdered)            #callinng updateShopOutputData() to update the output file for the current order
    openShop()                              #calling openShop() to ask for whether the shop is open


"""
Ready to take order or close the shop? Yes for open / No for close : yes
1 Vadai Rs. 10
2 Donut Rs. 40
3 Coke Rs. 50
4 Sandwich Rs. 25
5 Samosa Rs. 10
Attendent: How much of  Vadai  do you want?
Customer : 5
Attendent: How much of  Donut  do you want?
Customer : 1
Attendent: How much of  Coke  do you want?
Customer : 0
Attendent: How much of  Sandwich  do you want?
Customer : 2
Attendent: How much of  Samosa  do you want?
Customer : 3
Ready to take order or close the shop? Yes for open / No for close : yes
1 Vadai Rs. 10
2 Donut Rs. 40
3 Coke Rs. 50
4 Sandwich Rs. 25
5 Samosa Rs. 10
Attendent: How much of  Vadai  do you want?
Customer : 10
Attendent: How much of  Donut  do you want?
Customer : 2
Attendent: How much of  Coke  do you want?
Customer : 7
Attendent: How much of  Sandwich  do you want?
Customer : 3
Attendent: How much of  Samosa  do you want?
Customer : 0
Ready to take order or close the shop? Yes for open / No for close : no
"""