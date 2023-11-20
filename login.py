import pymongo
from pymongo.mongo_client import MongoClient
client = MongoClient("mongodb://localhost:27017/")

db = client["Users"]

collection =  db["Profiles"]
newUser = []
maxLengthList = 3
while len(newUser) < maxLengthList:
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    newUser.append(username)
    newUser.append(password)
print("Your account has been created")

    
result = db.profiles.insert_many(newUser)

verifyLogin = []
maxLengthList = 3
while len(verifyLogin) < maxLengthList:
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    verifyLogin.append(username, password) 

result  = db.profiles.find_one(verifyLogin)

#new



