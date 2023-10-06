import pymongo
client1 = pymongo.MongoClient('mongodb://localhost:27017/')
db1=client1['sundarpy']

col1=db1["sports1"]

x=col1.find_one()

print(x)

