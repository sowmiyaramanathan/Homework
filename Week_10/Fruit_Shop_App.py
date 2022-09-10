def displayItems():                                          #function to display fruits list
    for fruit in range(len(fruitList)):
        print(fruit + 1, fruitList[fruit])                   #printing fruits

def getOrder():
    customerChoice = True
    while(customerChoice != "That's all" and customerChoice != "No more"):      #reading order till customer says no more or that's all
        displayItems()                                                          #displaying fruits
        fruitFound = 0                                                          #intializing a boolean to track fruit
        quantityFound = 0                                                       #intializing a boolean to track fruit
        print("Vendor: What do you want?")                                      #asking for order
        customerOrder = input("Customer: ")                                     #reading order
        customerOrder = customerOrder.lower()                                   #converting the order to lowercase
        for fruit in range(len(fruitList)):                                     #iterating through the fruit list
            if customerOrder.__contains__(fruitList[fruit]):                    #checking the order for fruit
                fruitsOrdered.append(fruitList[fruit])                          #adding the order to the list
                fruitFound = 1                                        #changing the boolean as we have found the fruit
                break                                                 #stop iterating
        for quantity in quantityList:                                 #iterating the quantity list
            for quantityValue in quantity:                            #iterating items of the quantity list
                if customerOrder.__contains__(quantityValue):         #checking the order for the quantity
                    quantityOrdered.append(quantityValue)             #added the order to the list
                    quantityFound = 1                              #changing the boolean as we have found the quantity
                    break                                             #stop iterating
        if fruitFound and not quantityFound:                        #checking whether the quantity not found but fruit
            print("Vendor: How much of", fruitsOrdered[-1], "do you want?")     #asking for quantity
            customerOrder = input("Customer: ")                                #reading quantity for the fruit ordered
            quantityOrdered.append(customerOrder)                               #adding quantity to the list
        elif quantityFound and not fruitFound:                      #checking whether the fruit not found but quantity
            del quantityOrdered[-1]                                 #deleting the quantity from the list
            print("Vendor: The fruit is not available")             #telling the customer the fruit is not available
        elif not(fruitFound and quantityFound):                 #checking whether both fruit and quantitiy not found
            print("Vendor: Not available")                      #telling the customer the fruit is not available

        print("Vendor: Wanna order more? If not, type 'That's all' or 'No more'")   #asking for further orders
        customerChoice = input("Customer: ")                                        #reading input
    orderedItems = [list(item) for item in zip(fruitsOrdered, quantityOrdered)]     #merging the fruits and quantity ordered list into one
    return orderedItems                                                             #returing the final orders list
        
def printOrderDetails(orderItems):                                  #function to print order details
    if(len(orderItems) == 0):                                       #checking whether the customer has made any orders
        print("No orders made")                                     #printing no orders
    else:
        print("\nOrder Details:")
        for item in orderItems:                                     #looping the orders list
            print(item[0], ','.join(map(str, item[1:])))            #printing the orders

fruitList = ["apple", "orange", "banana", "cherry"]                 #initializing the fruits lits
quantityList = [["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"], ['1', '2', '3', '4', '5', '6', '7', '8', '9']]                                                 #initializing the quantity list
fruitsOrdered = []                                                   #declaring a list to store ordered fruits
quantityOrdered = []                                                 #declaring a list to store ordered quantity

orderDetails = getOrder()                                            #calling function to get orders
printOrderDetails(orderDetails)                                      #calling funciton to print order details

"""
1 apple
2 orange
3 banana
4 cherry
Vendor: What do you want?
Customer: 2 apple
Vendor: Wanna order more? If not, type 'That's all' or 'No more'
Customer: yes
1 apple
2 orange
3 banana
4 cherry
Vendor: What do you want?
Customer: 2 cherry
Vendor: Wanna order more? If not, type 'That's all' or 'No more'
Customer: yes
1 apple
2 orange
3 banana
4 cherry
Vendor: What do you want?
Customer: 3 banana
Vendor: Wanna order more? If not, type 'That's all' or 'No more'
Customer: yes
1 apple
2 orange
3 banana
4 cherry
Vendor: What do you want?
Customer: mango
Vendor: Not available
Vendor: Wanna order more? If not, type 'That's all' or 'No more'
Customer: No more

Order Details:
apple 2
cherry 2
banana 3
__________________________________________________________________________________________
test case 2

1 apple
2 orange
3 banana
4 cherry
Vendor: What do you want?
Customer: 7 Apple
Vendor: Wanna order more? If not, type 'That's all' or 'No more'
Customer: yes
1 apple
2 orange
3 banana
4 cherry
Vendor: What do you want?
Customer: 3 mango
Vendor: The fruit is not available
Vendor: Wanna order more? If not, type 'That's all' or 'No more'
Customer: yes
1 apple
2 orange
3 banana
4 cherry
Vendor: What do you want?
Customer: 4 banana
Vendor: Wanna order more? If not, type 'That's all' or 'No more'
Customer: yes
1 apple
2 orange
3 banana
4 cherry
Vendor: What do you want?
Customer: cherry 3
Vendor: Wanna order more? If not, type 'That's all' or 'No more'
Customer: yes
1 apple
2 orange
3 banana
4 cherry
Vendor: What do you want?
Customer: orange 10
Vendor: Wanna order more? If not, type 'That's all' or 'No more'
Customer: No more

Order Details:
apple 7
banana 4
cherry 3
orange 1
__________________________________________________________________________________________
test case 3

1 apple
2 orange
3 banana
4 cherry
Vendor: What do you want to buy?
Customer: apple
Vendor: How much apple do you want?
Customer: 3
Would you like to make another order? If not, 'Type 'That's all' or 'No more' ' : 
Customer: yes
1 apple
2 orange
3 banana
4 cherry
Vendor: What do you want to buy?
Customer: banana
Vendor: How much banana do you want?
Customer: 2
Would you like to make another order? If not, 'Type 'That's all' or 'No more' ' : 
Customer: yes
1 apple
2 orange
3 banana
4 cherry
Vendor: What do you want to buy?
Customer: mango
Enter valid fruit
Would you like to make another order? If not, 'Type 'That's all' or 'No more' ' :
Customer: That's all

Order Details:
apple 3
banana 2
"""