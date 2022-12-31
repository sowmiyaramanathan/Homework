from flask import Flask, request
from configparser import ConfigParser
import mysql.connector as msconnector

config = ConfigParser()
config.read("C:\\Users\\user\\Desktop\\Sayur Learning\\Sowmiya\\Mini_Project\\myproject\\backend\\connection.ini")
config_data  = config["credentials"]
try:
    mydatabase = msconnector.connect(
    host = config_data["host"],
    user = config_data["username"],
    password = config_data["password"],
    database = config_data["dbname"]
    )
    print("Connection made")
except:
    print("No connection made")

mycursor = mydatabase.cursor()
cursor = mydatabase.cursor(buffered=True)

app = Flask(__name__)

@app.route('/data')
def getData():
    return {
        'Name' : 'Sam'
    }

app.run()