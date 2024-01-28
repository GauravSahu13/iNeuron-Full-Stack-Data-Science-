import pymongo

client = pymongo.MongoClient("mongodb+srv://onShore:sahu9821@cluster0.a6ot5gp.mongodb.net/?retryWrites=true&w=majority")
db = client.test
database = client['myinfo']
collection = database["sudh"]


data = collection.find({"companyName" : "iNeuron"})        # pulling only company record
#data = collection.find({"courseOffered" :{"$gt" :"E"}})     # gt --> greater than or equal to E
for i in data :
    print(i)
