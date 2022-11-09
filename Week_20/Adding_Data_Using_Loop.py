"""Inserting fake data into a data base using loop"""

from configparser import ConfigParser       #importing configparser to configure credentials to establish connection to mysql data base
import mysql.connector as msconnector       #importing mysql.connector to connect mysql database
from faker import Faker                     #importing faker to generate fake data

config = ConfigParser()                     #initializing configparser method
config.read("C:\\Users\\user\Desktop\Sayur Learning\Sowmiya\Week_20\\connection.ini")   #reading the credentials file

config_data  = config["credentials"]            #initializing the credentials data

mydatabase = msconnector.connect(
    host = config_data["host"],
    user = config_data["username"],
    password = config_data["password"],
    database = config_data["dbname"]
)                                               #establishing connection to database

mycursor = mydatabase.cursor()                  #initializing cursor to the database

fake = Faker()                                  #initializing faker to generate fake data
dataToInsert = []                                        #declaring dataToInsert to store the fake data
dataCount = 1                                   #variable that is used to get 100 data
cursor = mydatabase.cursor(buffered=True)       #making the buffer to true to store the data 

while dataCount <= 100:                                 #loop to get 100 data
    dataCount += 1                                      #increasing the variable by 1
    dataToInsert.append(tuple([fake.first_name(), fake.last_name(), fake.city(), fake.state(), fake.phone_number()]))    #adding data to the dataToInsert variable as tuple

insertStatement = 'INSERT INTO `tblpersons` (personFirstName, personLastName, personCity, personState, personPhNo) VALUES ("%s", "%s", "%s", "%s", "%s");'          #initializing a variable that contains the insert statement

mycursor.executemany(insertStatement, dataToInsert)         #using executemany() to insert 100 data to the table
mydatabase.commit()                                         #commiting the changes

mycursor.execute('SELECT * FROM tblpersons')                #initializing mycursor to display the data in the table
myResult = mycursor.fetchall()                              #storing all the data as rows and columns in myResult

for data in myResult:                                          #loop to print the data
    print(data)                                                #printing the data