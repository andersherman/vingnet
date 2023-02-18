from typing import Union

from fastapi import FastAPI

PREFIX = "/fastapiexample"

app = FastAPI()


@app.get(PREFIX + "/")
def read_root():
    return {"Hello": "World"}


@app.get(PREFIX + "/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}
