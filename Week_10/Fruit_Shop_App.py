def getOrder(fruits, quantity):
    customerChoice = True
    fruitsOrder = []
    quantityOrder = []
    orderCount = 0
    while(customerChoice != "That's all" and customerChoice != "No more"):
        fruitFound = 0
        quantityFound = 0
        for fruit in range(len(fruits)):
            print(fruit + 1, fruits[fruit])
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



fruits = ["apple", "orange", "banana", "cherry"]
quantity = [["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"], ['1', '2', '3', '4', '5', '6', '7', '8', '9']]

orderItems = getOrder(fruits, quantity)
print("\nOrder Details: ")
for item in orderItems:
    print(item[0], ','.join(map(str, item[1:])))



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
"""