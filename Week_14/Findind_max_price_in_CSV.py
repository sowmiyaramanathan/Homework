file = open(r"C:\Users\user\Desktop\Sayur Learning\Sowmiya\Week_14\input.csv", "r")                     #opening the input file in read mode
priceIndex = 1           #setting the index value of price of the cafe items           
maximumPrice = 1                  #assigning maximumPrice value as 1

next(file)                        #skipping the header row
for item in file:                 #iterating through the file one line at a time
    temp = item.split(",")        #spiliting the line and storing it in a variable
    priceOfTheItem = int(temp[priceIndex])  #getting the price of the item
    if(maximumPrice <= priceOfTheItem):              #comparing it with the maximumPrice
        maximumPrice = priceOfTheItem                #if the maximumPrice is less, changing the maximumPrice to the current loop price

print("Maximum price in the list : ", maximumPrice)      #printing the maximumPrice

file.close()                                    #closing the file