# myDict = {
#     "car1" : {
#         "Brand" : "Toyota",
#         "Model" : "Corolla",
#         "Year" : 1995
#     },
#     "car2" : {
#         "Brand" : "Honda",
#         "Model" : "Civic",
#         "Year" : 2005
#     },
#     "car3" : {
#         "Brand" : "Honda",
#         "Model" : "Odyssey",
#         "Year" : 2020
#     }
# }
# print(myDict["car3"]["Model"])
# for x in myDict.values():
#     for y in x.values():
#         print(y)


myDict = {
    "apple" : {
        "Inventory" : 20,
        "MinCount" : 5,
        "ReCount" : 10
    },
    "banana" : {
        "Inventory" : 30,
        "MinCount" : 10,
        "ReCount" : 20
    },
    "orange" : {
        "Inventory" : 10,
        "MinCount" : 3,
        "ReCount" : 5
    }
}

inputFruit = input("Enter a fruit : ")
if inputFruit in myDict.keys():
    inputQuantity = int(input("Enter quantity : "))
    myDict[inputFruit]["Inventory"] -= inputQuantity
    print("Present supply of",inputFruit, "is", myDict[inputFruit]["Inventory"])
    if myDict[inputFruit]["Inventory"] < myDict[inputFruit]["MinCount"]:
        print("Time to refill", inputFruit, "by", myDict[inputFruit]["ReCount"])
        myDict[inputFruit]["Inventory"] += myDict[inputFruit]["ReCount"]
        print("After reorder inventory count : ", myDict[inputFruit]["Inventory"])
else:
    exit()