def openShop():                                                         #funtion to accept orders or close the shop
    open = input("Ready to take order or close shop? Yes for open /No for close: ")
    if(open == "No"):
        printTodayShopDetails()                                         #before closing printing sales details
        exit()                                                          #closing shop
    else:
        proceedRestock(originalSupply, currentSupply)                   #checking stock before taking orders
        displayMenu()                                                   #displaying menu
        takeOrder = True                                                     #getting order
    return takeOrder

def proceedRestock(startingSupply, presentSupply):                      #function to check stock and restocking
    global restockCount
    for supply in range(len(startingSupply)):
        quantityPresent = startingSupply[supply] * 0.2                  #calculating quantity limit to be present
        quantityToRestock = startingSupply[supply] - quantityPresent    #calculating how much to restock
        if(presentSupply[supply] <= quantityPresent):              #checking whether present supply is less than limit
            presentSupply[supply] += quantityToRestock                  #restocking the supply
            restockCount += 1                                      #calculating no of times supply has been restocked

def displayMenu():                                                      #function to display menu
    for item in range(len(cafeItems)):
        print(item + 1, cafeItems[item], "Rs.", itemsPrice[item])       #printing items list

def getOrder():                                                         #function to take orders
    for order in range(len(cafeItems)):
        print("Attendent: How much of ", (cafeItems[order]), " do you want?")  #asking for orders to the customer
        noOfItem = int(input("Customer: "))                                         #reading order
        if(noOfItem <= currentSupply[order]):                                       #checking for the supply
            currentSupply[order] -= noOfItem                                        #decreasing current supply
            noOfItemsSold[order] += noOfItem                                        #incresing items sold
            todaySales[order] += noOfItem * itemsPrice[order]                       #calculating sales
        else:
            print("Out of stock")                                            #printing no stock in case of less supply

def printTodayShopDetails():                                            #function to print sales details
    print("Today sales : ", sum(todaySales))                            #printing sales
    print("No of items sold : ", noOfItemsSold)                         #printing number of items sold
    print("The supply has been restocked : ", restockCount, "times") #printing no. times the supply has been restocked


cafeItems = ["Cookies", "Donut", "Cake", "Coffee"]        #initializing items
itemsPrice = [30, 50, 70, 20]                             #initializing items price
originalSupply = [25, 25, 25, 25]                         #initializing original supply at the start of the day
currentSupply = [25, 25, 25, 25]                          #initializing current supply to track supply for each orders
noOfItemsSold = [0, 0, 0, 0]                              #initializing number of items sold
todaySales = [0, 0, 0, 0]                                 #initializing sales for the day
restockCount = 0                                          #initializing restock count to keep track of restock

openToOrder = openShop()                                                #calling openshop function to get orders
while(openToOrder == True):
    getOrder()
    openShop()



"""
test case 1
Ready to take order or close shop? Yes for open /No for close: No
Today sales :  0
No of items sold :  [0, 0, 0, 0]
The supply has been restocked :  0 times
__________________________________________
test case 2
Ready to take order or close shop? Yes for open /No for close: Yes
1 Cookies Rs. 30
2 Donut Rs. 50
3 Cake Rs. 70
4 Coffee Rs. 20
Attendent: How much of Cookies do you want?
Customer: 2
Attendent: How much of Donut do you want?
Customer: 1
Attendent: How much of Cake do you want?
Customer: 0
Attendent: How much of Coffee do you want?
Customer: 2
Ready to take order or close shop? Yes for open /No for close: Yes
1 Cookies Rs. 30
2 Donut Rs. 50
3 Cake Rs. 70
4 Coffee Rs. 20
Attendent: How much of Cookies do you want?
Customer: 4
Attendent: How much of Donut do you want?
Customer: 10
Attendent: How much of Cake do you want?
Customer: 3
Attendent: How much of Coffee do you want?
Customer: 0
Ready to take order or close shop? Yes for open /No for close: No
Today sales :  980
No of items sold :  [6, 11, 3, 2]
The supply has been restocked :  0 times
_____________________________________

test case 2
Ready to take order or close shop? Yes for open /No for close: Yes
1 Cookies Rs. 30
2 Donut Rs. 50
3 Cake Rs. 70
4 Coffee Rs. 20
Attendent: How much of Cookies do you want?
Customer: 25
Attendent: How much of Donut do you want?
Customer: 23
Attendent: How much of Cake do you want?
Customer: 10
Attendent: How much of Coffee do you want?
Customer: 20
Ready to take order or close shop? Yes for open /No for close: Yes
1 Cookies Rs. 30
2 Donut Rs. 50
3 Cake Rs. 70
4 Coffee Rs. 20
Attendent: How much of Cookies do you want?
Customer: 12
Attendent: How much of Donut do you want?
Customer: 29
Out of stock
Attendent: How much of Cake do you want?
Customer: 15
Attendent: How much of Coffee do you want?
Customer: 2
Ready to take order or close shop? Yes for open /No for close: No
Today sales :  4450
No of items sold :  [37, 23, 25, 22]
The supply has been restocked :  3 times
"""