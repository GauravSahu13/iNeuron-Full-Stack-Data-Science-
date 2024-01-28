import pymongo
data =  [
        {
            "item": "canvas",
            "qty": 100,
            "size": {"h": 28, "w": 35.5, "uom": "cm"},
            "status": "A",
        },
        {
            "item": "journal",
            "qty": 25,
            "size": {"h": 14, "w": 21, "uom": "cm"},
            "status": "A",
        },
        {
            "item": "mat",
            "qty": 85,
            "size": {"h": 27.9, "w": 35.5, "uom": "cm"},
            "status": "A",
        },
        {
            "item": "mousepad",
            "qty": 25,
            "size": {"h": 19, "w": 22.85, "uom": "cm"},
            "status": "P",
        },
        {
            "item": "notebook",
            "qty": 50,
            "size": {"h": 8.5, "w": 11, "uom": "in"},
            "status": "P",
        },
        {
            "item": "paper",
            "qty": 100,
            "size": {"h": 8.5, "w": 11, "uom": "in"},
            "status": "D",
        },
        {
            "item": "planner",
            "qty": 75,
            "size": {"h": 22.85, "w": 30, "uom": "cm"},
            "status": "D",
        },
        {
            "item": "postcard",
            "qty": 45,
            "size": {"h": 10, "w": 15.25, "uom": "cm"},
            "status": "A",
        },
        {
            "item": "sketchbook",
            "qty": 80,
            "size": {"h": 14, "w": 21, "uom": "cm"},
            "status": "A",
        },
        {
            "item": "sketch pad",
            "qty": 95,
            "size": {"h": 22.85, "w": 30.5, "uom": "cm"},
            "status": "A",
        },
    ]

client = pymongo.MongoClient("mongodb+srv://onShore:sahu9821@cluster0.a6ot5gp.mongodb.net/?retryWrites=true&w=majority")
db = client.test
database = client['inventory']
collection = database["table"]
#collection.insert_many(data)
#d = collection.find({'status':'A'})

#d = collection.find({'status':{'$in':['A' , 'P']}})      # $in -> filter  condition
                                                        # $nin --> not in filter condition

#d = collection.find({'status':{"$gt" : "C"}})        # gt --> greater than

#d = collection.find({'qty':{'$gte' :75}})            # gte --> greater than & equal to

#d = collection.find({'item': 'sketch pad','qty': 95})

#d = collection.find({ 'item': 'sketch pad' , 'qty' :{"$gte" : 75}})

#d = collection.find({'$or' : [{ 'item': 'sketch pad'} , {'qty': {"$gte": 75}}]})      # or condition

# $all --> used in nested json for array in collection

#d = collection.find({'size.h' : 8.5})     # nested array

# count and limit method
#d = collection.find().limit((3))

# sorting of data
#d = collection.find().sort({ 'item' : 1 })     # ascending order
#d = collection.find().sort({ 'item' : -1 })     # descending order

# Updating one value
#collection.update_one({'item': 'canvas'} , {'$set':{'item': 'sudhanshu'} })
#$inc: 2  --> increment by 2

# replace
'''collection.replace_one({"item" : "postcard"},
                       {"item" : "postcard",
                        "qty": 60,
                        "size": {"h": 20, "w": 15, "uom": "am"},
                        "status": "D"
                        })'''

# Deleting one value
#collection.delete_one({'item': 'sudhanshu'})

#d = collection.find({'item': 'postcard'})

for i in d :
    print(i)

