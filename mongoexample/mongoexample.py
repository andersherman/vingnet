#!/usr/bin/env python3

from pprint import pprint
from pymongo import MongoClient

MONGODB_URI = "mongodb://localhost:27017"

# Connect to your MongoDB cluster:
client = MongoClient(MONGODB_URI)

# List all the databases in the cluster:
print("Databases:")
for db_info in client.list_database_names():
   print(db_info)
print()

def insert(collection):
    docs = [
        {"_id": 1, "title": "This is number 1"},
        {"_id": 2, "title": "This is number 2"},
        {"_id": 3, "title": "This is number 3"},
        {"_id": 4, "title": "This is number 4"},
    ]
    insert_result = collection.insert_many(docs)
    print("Inserted", insert_result)

def find_index(collection, id):
    print("FIND", id, collection[id])

def find_doc(collection, text, doc):
    print("FIND", text)
    for doc in collection.find(doc):
        pprint(doc)

db = client['mytest']
coll = db['coll']

#insert(coll)
#find_index(coll, 1)
find_doc(coll, "First doc before change", {"_id": 1})
coll.replace_one({'_id': 1}, {'title': 'This is number 1 updated again'}, upsert=True)
#coll.replace_one({'title': 'This is number 1'}, {'title': 'This is number 1 updated'}, upsert=True)
find_doc(coll, "First doc", {"_id": 1})

find_doc(coll, "Rest", {'_id': {'$gt': 1}})

docs = list(coll.find({}))
print("DOCS", docs)
