class Items():
    name = ""

    def __init__(self, name):
        self.name = name
        self.collectData()

    def collectData(self):
        self.totalQuantity = int(input("How much of " + self.name + " is present? "))
        self.totalSales = int(input("How much of " + self.name + " has been sold? "))
        self.balanceQuantity = self.totalQuantity - self.totalSales

totalItems = int(input("How many items are available : "))

itemsName = []
for item in range(totalItems):
    itemsName.append(input("Item name : "))

itemsData = {}
for name in itemsName:
    item = '{}'.format(name)
    itemsData[item] = itemsData.get(item, Items(name))

for item in itemsName:
    print("1. " + item)

input = input("Enter the item name to get details ")

for item in itemsData.keys():
    if input == item:
        food = itemsData.get("coke")
        print(food.o)