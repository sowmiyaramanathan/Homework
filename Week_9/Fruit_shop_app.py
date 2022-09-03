fruitsList = ["apple", "orange", "banana", "melon", "cherry"]
customerNeed = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

fruit = None
quantity = None
customer = True

print("Fruits: \n1. apple\n2.orange\n3.banana\n5.melon\n6.cherry")
while(customer == True):
    print("Vendor: What do you want?")
    customerResponse = input("Customer: ")
    customerResponse = customerResponse.lower().split()
    for response in range(len(customerResponse)):
        if customerResponse[response] in fruitsList:
            fruit = customerResponse[response]
        elif customerResponse[response] in customerNeed:
            quantity = customerResponse[response]
    if(fruit == None):
        print("The item you are asking is not available. Do you want anything from the list. Yes/No")
        customerChangeResponse = input()
        if(customerChangeResponse == "Yes"):
            customer = True
        else:
            customer = False
    else:
        customer = False
        
if(fruit != None and quantity == None):
    print("How much of ", fruit, "do you want? ")
    quantity = int(input())

print(customerResponse)
print("Customer ordered : ")
print("Fruit : ", fruit)
print("Quantity : ", quantity)