from configparser import ConfigParser
import mysql.connector as msconnector
from faker import Faker

config = ConfigParser()
config.read("C:\\Users\\user\Desktop\Sayur Learning\Sowmiya\Week_20\\connection.ini")

config_data  = config["credentials"]

mydatabase = msconnector.connect(
    host = config_data["host"],
    user = config_data["username"],
    password = config_data["password"],
    database = config_data["dbname"]
)

mycursor = mydatabase.cursor()

fake = Faker()
row= {}
n = 0
cursor = mydatabase.cursor(buffered=True)

while n <= 100:
    n += 1
    row = [fake.first_name(), fake.last_name(), fake.city(), fake.state(), fake.phone_number()]
    mycursor.execute('INSERT INTO `tblpersons` (personFirstName, personLastName, personCity, personState, personPhNo) VALUES ("%s", "%s", "%s", "%s", "%s");' %(row[0], row[1], row[2], row[3], row[4]))

print("iteration is ", n - 1)
mydatabase.commit()