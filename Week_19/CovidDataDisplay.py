from configparser import ConfigParser       #importing configparser to configure credentials to establish connection to mysql data base
import mysql.connector as msconnector       #importing mysql.connector to connect mysql database

config = ConfigParser()                     #initializing configparser method
config.read("C:\\Users\\user\Desktop\Sayur Learning\Sowmiya\Week_19\\connection.ini")   #reading the credentials file

config_data  = config["credentials"]            #initializing the credentials data

mydatabase = msconnector.connect(
    host = config_data["host"],
    user = config_data["username"],
    password = config_data["password"],
    database = config_data["dbname"]
)                                               #establishing connection to database

mycursor = mydatabase.cursor()                  #initializing cursor to the database

# mycursor.execute('SELECT city FROM tbl_coviddata ORDER BY affected DESC')    #initializing mycursor to order the cities in descending order by affected case
# myResult = mycursor.fetchone()                              #getting the first data and storing it in a variable
# print("City with most affected case : ", *myResult)         #printing the most affected city

# mycursor.reset()
# mycursor.execute('SELECT city FROM tbl_coviddata ORDER BY recovered DESC')    #initializing mycursor to order the cities in descending order by recovered case
# myResult = mycursor.fetchone()                                #getting the first data and storing it in a variable
# print("City with high recovery status : ", *myResult)         #printing the most affected city


# data = [("India", "TamilNadu", "KanyaKumari", 14000, 10000, "15-30", "20%"),
#         ("India", "TamilNadu", "Karur", 12400, 9000, "20-60", "15%"),
#         ("India", "TamilNadu", "Dindugal", 12000, 5400, "30-50", "21%"),
#         ("India", "TamilNadu", "Theni", 17000, 7000, "45-74", "40%")]

# insertStatement = 'INSERT INTO tbl_coviddata VALUES (%s, %s, %s, %s, %s, %s, %s)'

# mycursor.executemany(insertStatement, data)
# mydatabase.commit()

# mycursor.execute("UPDATE tbl_coviddata set deathrate = replace(deathrate, "%", "")")
mycursor.execute('select city from tbl_coviddata order by convert(deathrate, decimal) desc')
result = mycursor.fetchmany(size = 3)
for x in result:
    print(x)

# mydatabase.commit()