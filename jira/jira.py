#!/usr/bin/env python3

from pprint import pprint
from pymongo import MongoClient, TEXT

client = MongoClient("mongodb://localhost:27017")

# List all the databases in the cluster:
print("Databases:")
for db_info in client.list_database_names():
   print(db_info)
print()

def insert(coll):
    docs = [
        {"_id": "JIRA-1", "title": "This is number 1", "alm": [1, 2, 3]},
        {"_id": "JIRA-2", "title": "This is number 2", "alm": [2, 3]},
        {"_id": "JIRA-3", "title": "This is number 3", "alm": [3, 4, 5]},
        {"_id": "JIRA-4", "title": "This is number 4", "alm": []},
    ]
    insert_result = coll.insert_many(docs)
    print("Inserted", insert_result)

def find_index(collection, id):
    print("FIND", id, collection[id])

def find_doc(collection, text, doc):
    print("FIND", text)
    for doc in collection.find(doc):
        pprint(doc)

coll = client['jira']['coll']
coll.create_index([('title', TEXT)])

#insert(coll)
#find_index(coll, 1)
#find_doc(coll, "First doc before change", {"_id": 1})
#coll.replace_one({'_id': 1}, {'title': 'This is number 1 updated again'}, upsert=True)
#coll.replace_one({'title': 'This is number 1'}, {'title': 'This is number 1 updated'}, upsert=True)
#find_doc(coll, "First doc", {"_id": 1})

find_doc(coll, "All", {})

find_doc(coll, "With ALM#5", {'alm': 5})

find_doc(coll, "With text", { '$text': { '$search': "number"}})
