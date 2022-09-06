items = ["Cookies", "Donut", "Cake", "Coffee"]
price = [30, 50, 70, 20]
supply = [25, 25, 25, 25]

def sales():
    customerChoice = "Yes"
    sales = [0, 0, 0, 0]
    countRestock = 0
    maxTransaction = 10
    while(maxTransaction>0 and customerChoice == "Yes"):
        for item in range(len(items)):
            print(item + 1, items[item], " Rs.", price[item])
        
        for order in range(len(items)):
            print("How much of " + str(items[order]) + " do you want?")
            orderItem = int(input("Customer: "))
            if(orderItem <= supply[order]):
                supply[order] -= orderItem
                sales[order] += orderItem * price[order]
        
        # restockMark = 0.2
        # for supplyIndex in range(len(supply)):
        #     if(supply[supplyIndex] <= (supply[supplyIndex]*restockMark)):
        #         supply[supplyIndex] += supply[supplyIndex] * restockMark
        #         countRestock += 1
        #         print("Restocked")
        maxTransaction -= 1
        print("Attendant: Would like to order again? Yes/No")
        customerChoice = input("Customer: ")
        # print("The supply has been restocked", countRestock, "times")
        print("\n\nSales of the shop:")
        return sales

sales = sales()
print(*sales)