"""Write an app for the fruit vendor. Fruit vendor has a list of fruits (apple, Orange, banana etc). When the customer comes in, vendor asks "What do you want to buy?". The customer can say "I want apple", or "Apple" or "three apple" or something like that. Your program will find out what fruit the customer is asking. 
Your program will also find, if the customer already asked for the quantity of the fruit (one apple or 5 orange etc). Print the quantity if the customer says the quantity. If not, ask him how much he wants. You can limit the quantity to single digit number."""

fruitsList = ["apple", "orange", "banana", "melon", "cherry"]       #initializing fruits list
quantityWord = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"] #initializing quantity in english
quantityNumeric = ['1', '2', '3', '4', '5', '6', '7', '8', '9']         #initializing quantity in numeric

fruitNeed = None                #initializing fruits needed by customer as none
quantityNeed = None             #initializing fruits needed by customer as none
customer = True                 #initialzing boolean to indicate that there is customer who is going to order

for fruit in range(len(fruitsList)):            #printing available fruits
    print(fruit+1, fruitsList[fruit])


while(customer == True):                        #customer is ready to order
    print("Vendor: What do you want?")          #asking what the customer wants
    customerResponse = input("Customer: ")      #reading customer response
    customerResponse = customerResponse.lower().split()         #converting the response into lowercase and list
    for response in range(len(customerResponse)):               #looping through the response list to find what the customer has ordered
        if customerResponse[response] in fruitsList:            #checking if the response has available fruit
            fruitNeed = customerResponse[response]
        elif customerResponse[response] in quantityWord or quantityNumeric:            #checking if the response has quantity of fruit
            quantityNeed = customerResponse[response]
    if(fruitNeed == None):                                      #checking whether the fruit is not available
        quantityNeed = None
        print("Vendor: The item you are asking is not available. Do you want anything from the list. Yes/No")   #asking if the customer wants order something that is in the list only
        customerChangeResponse = input("Customer: ")            #reading the customer input for reordering
        if(customerChangeResponse == "No"):         #checking if the customer wants to not order again
            customer = False                        #changing the boolean value to close the order
    else:                                           #in case the fruit is available, close the order
        customer = False
        
if(fruitNeed != None and quantityNeed == None):     #checking whether the fruit is ordered and the quantity is not specified
    print("Vendor: How much of", fruitNeed, "do you want? ")    #asking for the quantity
    quantityNeed = (input("Customer: "))                         #reading the quantity

#printing the order details
print("Customer ordered : ")
print("Fruit : ", fruitNeed)
print("Quantity : ", quantityNeed)



"""
test case 1
1 apple
2 orange
3 banana
4 melon
5 cherry
Vendor: What do you want?
Customer: one apple
Customer ordered : 
Fruit :  apple
Quantity :  one
________________________________
test case 2
1 apple
2 orange
3 banana
4 melon
5 cherry
Vendor: What do you want?
Customer: One mango
Vendor: The item you are asking is not available. Do you want anything from the list. Yes/No
Customer: Yes
Vendor: What do you want?
Customer: One cherry
Customer ordered : 
Fruit :  cherry
Quantity :  one
_________________________________
test case 3
1 apple
2 orange
3 banana
4 melon
5 cherry
Vendor: What do you want?
Customer: banana
Vendor: How much of banana do you want? 
Customer: 23
Customer ordered : 
Fruit :  banana
Quantity :  23
__________________________________
test case 4
1 apple
2 orange
3 banana
4 melon
5 cherry
Vendor: What do you want?
Customer: lemon
Vendor: The item you are asking is not available. Do you want anything from the list. Yes/No
Customer: No
Customer ordered : 
Fruit :  None
Quantity :  None
__________________________________
test case 5
1 apple
2 orange
3 banana
4 melon
5 cherry
Vendor: What do you want?
Customer: I want two orange
Customer ordered : 
Fruit :  orange
Quantity :  two
__________________________________
test case 6
1 apple
2 orange
3 banana
4 melon
5 cherry
Vendor: What do you want?
Customer: 5 banana
Customer ordered : 
Fruit :  banana
Quantity :  5
"""