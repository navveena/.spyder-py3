import pymongo

client1 = pymongo.MongoClient('mongodb://localhost:27017/')
db1=client1["naveena"]

c1=db1["fruits"]

d11=c1.find().sort("price",-1)

for x in d11:
    print(x)
    
d11=c1.find().sort("price",1)

for x in d11:
    print(x)