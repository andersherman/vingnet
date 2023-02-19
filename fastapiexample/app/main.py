from typing import Union

from fastapi import FastAPI
from pymongo import MongoClient

PREFIX = "/fastapiexample"

app = FastAPI()

db_client = MongoClient("mongodb://mongo:27017")
collection = db_client["fastapiexample"]["mycollection"]

@app.get(PREFIX + "/")
def read_root():
    return {"Hello": "World"}

@app.get(PREFIX + "/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    global collection
    return collection.find_one({"_id": item_id})
    # return {"item_id": item_id, "q": q}
