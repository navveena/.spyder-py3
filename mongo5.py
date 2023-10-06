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

#change
q1={"name":"apple"}
q2={"$set":{"price":13200}}
c1.update_one(q1,q2)

#delete
q1={"name":"orange"}
c1.delete_one(q1)

#change all
q={"name":"orange"}
qy={"$set":{"price":400}}
c1.update_many(q,qy)

for a in c1.find():
    print(a)