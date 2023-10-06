import pymongo

clientnew = pymongo.MongoClient('mongodb://localhost:27017/')
db1=clientnew["naveena"]

#collections create

c1=db1["fruits"]

fru=[
    
 {"name":"apple","price":260,"qty":"1kg"},
 {"name":"apple","price":260,"qty":"1kg"},
 {"name":"apple","price":260,"qty":"1kg"}]

x=c1.insert_many(fru)
for x in fru:
    print(x)