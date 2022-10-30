# import mysql.connector
# mydb = mysql.connector.connect(
#   host="localhost",
#   user="sayur_user",
#   password="Sayur!23",
#   database="sayur_db"
# )


# mycursor = mydb.cursor()

# mycursor.execute("CREATE TABLE Fruit_Details (fruit_id INTEGER, name VARCHAR(255), color VARCHAR(255), cost DECIMAL(5,2), city VARCHAR(255))")
# mycursor.execute("CREATE TABLE Fruit_Inventory(fruit_id INTEGER, quantity INTEGER, min_inventory INTEGER, reorder_qty INTEGER)")
# mycursor.execute("SHOW TABLES")

# for x in mycursor:
#     print(x)

# mycursor.execute("INSERT INTO Fruit_Details VALUES (1, 'Apple', 'Red',15.50, 'Hyderabad')");
# mycursor.execute("INSERT INTO Fruit_Details VALUES (1, 'Banana', 'Yellow',5.50, 'Chennai')");
# mycursor.execute("INSERT INTO Fruit_Details VALUES (1, 'Orange', 'Orange',20.25, 'Bangalore')");

# mydb.commit()

# mycursor.execute("SELECT * FROM  Fruit_Inventory")
# mycursor.execute("SELECT  \
#                     Fruit_Details.name, \
#                     Fruit_Details.color, \
#                     Fruit_Inventory.quantity \
#                     FROM  Fruit_Details INNER JOIN Fruit_Inventory \
#                     ON Fruit_Details.fruit_id = Fruit_Inventory.fruit_id")


# myresult = mycursor.fetchall()

# for x in myresult:
#     print(x)
# # https://www.w3schools.com/python/python_mysql_getstarted.asp

import random
name = input("Enter your name : ")
print("Good luck ", name)
words = ['cat', 'dog', 'anime', 'water', 'night']
level = 1
word = random.choice(words)
length = 3

while level <= 3:
    while len(word) <= length:
        word = random.choice(words)
    guesses = 0
    index = 1
    turns = 1
    while turns <= 5:
        guess = input("Guess a character ")
        if guess == word[index]:
            print("G")
            guesses += 1
            index += 1
        elif guess in word:
            print("Y")
        elif guess not in word:
            print("R")
            turns += 1
        print("You have", turns)
    if guesses == len(word):
        print("You won", word)
        length += 1
        level += 1
    else:
        print("you lose")
        exit()
