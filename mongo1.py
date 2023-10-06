import pymongo

client1 = pymongo.MongoClient('mongodb://localhost:27017/')

print("mongodb connected with python successfully")

db1 = client1['usamayurnewsundarpy1']

col1=db1["sports"]

dict1={"name":"sachin","sportsname":"cricket"}

x= col1.insert_one(dict1)

print(x)

for x1 in col1.find():
    print(x1)