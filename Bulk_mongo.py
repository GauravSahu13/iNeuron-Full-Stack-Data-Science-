import pandas as pd
import pymongo
import json


fitbit= pd.read_csv(r"C:\Users\sahus\Downloads\Gaurav\FitBit data.csv")
# converting into json
'''The issue regarding bulk upload to mongoDB was that it was creating a single document inside our collection.
 So here the trick is while converting CSV to JSON we need to mention orient as records. Thats it. Each record will be
 a separate document in mondodb.'''

fitbit.to_json(r"C:\Users\sahus\Downloads\Gaurav\new_FitBitdat.json",orient="records")
df_read_json = pd.read_json(r"C:\Users\sahus\Downloads\Gaurav\new_FitBitdat.json")
#print(df_read_json.head())

# Q) load the JSON, and store it in data.
#  P.S - the data here is stored as list, unlike dictionary if the JSON was not specified as records earlier.

with open(r"C:\Users\sahus\Downloads\Gaurav\new_FitBitdat.json") as file:
    data = json.load(file)
#print(data[0:5])




# connecting with mongodb
client = pymongo.MongoClient("mongodb+srv://onShore:sahu9821@cluster0.a6ot5gp.mongodb.net/?retryWrites=true&w=majority")
db_mongo = client['FitBit']
#print(db_mongo)

# bulk upload to mongoDB
collection = db_mongo['newfitbitdata']
collection.insert_many(data)
#print(collection)

#the above push was success. Lets try to fetch some collections from mongodb
record_ex1 = collection.find({"Id": 1503960366})
list_record =[]
for i in record_ex1:
    list_record.append(i)
l= list_record[:2]
df= pd.DataFrame(l)
print(df)
