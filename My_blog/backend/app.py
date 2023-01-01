from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
from passlib.hash import sha256_crypt
from configparser import ConfigParser
# import mysql.connector as msconnector

# config = ConfigParser()
# config.read("C:\\Users\\user\\Desktop\\Sayur Learning\\Sowmiya\\My_blog\\backend\\blogDB\\connection.ini")
# config_data  = config["credentials"]
# try:
#     mydatabase = msconnector.connect(
#     host = config_data["host"],
#     user = config_data["username"],
#     password = config_data["password"],
#     database = config_data["dbname"]
#     )
#     print("Connection made")
# except:
#     print("No connection made")

# mycursor = mydatabase.cursor()
# cursor = mydatabase.cursor(buffered=True)

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS' ] = 'Content-Type'

@app.route('/signupdetails', methods=["POST"])
def signupdetails():
    name = request.json.get('name', None)
    print(name)
    userName = request.json.get('userName', None)
    print(userName)
    return jsonify({'msg': 'signed up successfully'})

app.run()