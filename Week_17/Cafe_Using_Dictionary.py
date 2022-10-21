itemsData = {
    "Sandwich" : {
        "Price" : 40,
        "Supply" : 100,
        "Sales" : 0
    },
    "Donut" : {
        "Price" : 50,
        "Supply" : 100,
        "Sales" : 0
    },
    "Coke" : {
        "Price" : 30,
        "Supply" : 100,
        "Sales" : 0
    }
}
maxTransaction = 10
openToOrder = 'yes'

for item in itemsData.keys():
    print(item, " - Rs.", itemsData[item]["Price"])
    
while maxTransaction > 0 and openToOrder == "yes":
    for item in itemsData.keys():
        noOfItem = int(input("How much " + item + " do you want? "))
        if noOfItem <= itemsData[item]["Supply"]:
            itemsData[item]["Supply"] -= noOfItem
            itemsData[item]["Sales"] += noOfItem * itemsData[item]["Price"]
        else:
            print("Out of stock")
    maxTransaction -= 1
    openToOrder = input("Open to receive orders (yes / no) : ")

for item in itemsData.keys():
    print("Sales in ", item, " - ", itemsData[item]["Sales"])

"""
test case 1
Sandwich  - Rs. 40
Donut  - Rs. 50
Coke  - Rs. 30
How much Sandwich do you want? 150
Out of stock
How much Donut do you want? 10
How much Coke do you want? 0
Open to receive orders (yes / no) : no
Sales in  Sandwich  -  0
Sales in  Donut  -  500
Sales in  Coke  -  0
____________________________________________
test case 2
Sandwich  - Rs. 40
Donut  - Rs. 50
Coke  - Rs. 30
How much Sandwich do you want? 20
How much Donut do you want? 30
How much Coke do you want? 20
Open to receive orders (yes / no) : yes
How much Sandwich do you want? 1
How much Donut do you want? 1
How much Coke do you want? 1
Open to receive orders (yes / no) : no
Sales in  Sandwich  -  840
Sales in  Donut  -  1550
Sales in  Coke  -  630
____________________________________________
"""
