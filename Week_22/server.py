from flask import Flask, render_template, request
from configparser import ConfigParser       #importing configparser to configure credentials to establish connection to mysql data base
import mysql.connector as msconnector       #importing mysql.connector to connect mysql database

config = ConfigParser()                     #initializing configparser method
config.read("C:\\Users\\user\Desktop\Sayur Learning\Sowmiya\Week_22\\connection.ini")   #reading the credentials file
config_data  = config["credentials"]            #initializing the credentials data
mydatabase = msconnector.connect(
    host = config_data["host"],
    user = config_data["username"],
    password = config_data["password"],
    database = config_data["dbname"]
)                                               #establishing connection to database
mycursor = mydatabase.cursor()                  #initializing cursor to the database
cursor = mydatabase.cursor(buffered=True)       #making the buffer to true to store the data 

app = Flask(__name__)

@app.route('/selectchoice')
def choice():
    return render_template('choice.html')

@app.route('/addproducts')
def add():
    return render_template('add.html')

@app.route('/addproduct', methods = ["POST"])
def adding():
    kolejPazarID = request.form.get("kolejPazarID")
    prdtName = request.form.get("prdtName")
    prdtBrand = request.form.get("prdtBrand")
    prdtDescrp = request.form.get("prdtDescrp")
    prdtMRP = request.form.get("prdtMRP")
    prdtSP = request.form.get("prdtSP")
    prdtMarg = request.form.get("prdtMarg")
    prdtStk = request.form.get("prdtStk")
    add = (kolejPazarID, prdtName, prdtBrand, prdtDescrp, int(prdtMRP), int(prdtSP), int(prdtMarg), int(prdtStk))
    print(add)
    insertStatement = 'INSERT INTO `tbl_products` (kolejPazarID, productName, productBrand, productDescription, productProfitMargin, productMRP, productSP, productInStock) VALUES (%s, %s, %s, %s, %s, %s, %s, %s);'
    mycursor.execute(insertStatement, add)
    mydatabase.commit()
    return ''
 
@app.route('/viewproducts')
def view():
    return render_template('view.html')

@app.route('/view')
def viewPrdts():
    data = []
    mycursor.execute('SELECT * FROM tbl_products')
    result = mycursor.fetchall()
    for index in result:
        data.append(index)
    return data

app.run()