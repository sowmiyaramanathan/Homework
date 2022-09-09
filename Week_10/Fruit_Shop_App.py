def printMenu(fruitsMenu):
    for fruit in range(len(fruitsMenu)):
        print(fruit + 1, fruitsMenu[fruit])

def getOrder(fruits, quantity):
    customerChoice = True
    fruitsOrder = []
    quantityOrder = []
    orderCount = 0
    while(customerChoice != "That's all" and customerChoice != "No more"):
        fruitFound = 0
        quantityFound = 0
        printMenu(fruits)
        print("Vendor: What do you want to buy?" )
        customerOrder = input("Customer: ")
        customerOrder = customerOrder.lower().split()
        orderCount += 1
        
        for order in range(len(customerOrder)):
            if customerOrder[order] in fruits:
                fruitsOrder.append(customerOrder[order])
                fruitFound = 1
            else:
                if(any(customerOrder[order] in quan for quan in quantity)):
                    quantityOrder.append(customerOrder[order])
                    quantityFound = 1
        
        if quantityFound and not fruitFound:
            del quantityOrder[-1]
            print("Vendor: The fruit is not available")
        elif fruitFound and not quantityFound:
            print("Vendor: How much", fruitsOrder[-1], "do you want?")
            customerOrder = input("Customer: ")
            quantityOrder.append(customerOrder)
        elif not(fruitFound and quantityFound):
            print("Enter valid fruit")

        print("Would you like to make another order? If not, 'Type 'That's all' or 'No more' ' : ")
        customerChoice = input("Customer: ")
    orderItems = [list(item) for item in zip(fruitsOrder, quantityOrder)]
    return orderItems

def printOrder(items):
    if(len(items) == 0):
        print("No orders taken")
    else:
        print("\nOrder Details: ")
        for item in items:
            print(item[0], ','.join(map(str, item[1:])))



fruits = ["apple", "orange", "banana", "cherry"]
quantity = [["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"], ['1', '2', '3', '4', '5', '6', '7', '8', '9']]

orderItems = getOrder(fruits, quantity)
printOrder(orderItems)


"""
test case 1
1 apple
2 orange
3 banana
4 cherry
Vendor: What do you want to buy?
Customer: 2 apple
Would you like to make another order? If not, 'Type 'That's all' or 'No more' ' : 
Customer: yes
1 apple
2 orange
3 banana
4 cherry
Vendor: What do you want to buy?
Customer: 2 cherry
Would you like to make another order? If not, 'Type 'That's all' or 'No more' ' : 
Customer: 3 banana
1 apple
2 orange
3 banana
4 cherry
Vendor: What do you want to buy?
Customer: 3 banana
Would you like to make another order? If not, 'Type 'That's all' or 'No more' ' : 
Customer: yes
1 apple
2 orange
3 banana
4 cherry
Vendor: What do you want to buy?
Customer: yes
Vendor: The fruit is not available
Would you like to make another order? If not, 'Type 'That's all' or 'No more' ' :
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
Vendor: What do you want to buy?
Customer: 7 apple
Would you like to make another order? If not, 'Type 'That's all' or 'No more' ' : 
Customer: yes
1 apple
2 orange
3 banana
4 cherry
Vendor: What do you want to buy?
Customer: 3 mango
Vendor: The fruit is not available
Would you like to make another order? If not, 'Type 'That's all' or 'No more' ' :
Customer: 4 banana
1 apple
2 orange
3 banana
4 cherry
Vendor: What do you want to buy?
Customer: 4 banana
Would you like to make another order? If not, 'Type 'That's all' or 'No more' ' : 
Customer: yes
1 apple
2 orange
3 banana
4 cherry
Vendor: What do you want to buy?
Customer: cherry
Vendor: How much cherry do you want?
Customer: 3
Would you like to make another order? If not, 'Type 'That's all' or 'No more' ' : 
Customer: yes
1 apple
2 orange
3 banana
4 cherry
Vendor: What do you want to buy?
Customer: 3
Vendor: The fruit is not available
Would you like to make another order? If not, 'Type 'That's all' or 'No more' ' :
Customer: No more

Order Details:
apple 7
banana 4
cherry 3
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