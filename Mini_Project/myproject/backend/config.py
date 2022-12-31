from configparser import ConfigParser

config = ConfigParser()

config["credentials"] = {
    "host" : "localhost",
    "dbname" : "users_data",
    "username" : "edupad",
    "password" : "Sowmiya@2002"
}

with open(r"C:\Users\user\Desktop\Sayur Learning\Sowmiya\Mini_Project\server\connection.ini", "w") as f:
    config.write(f)