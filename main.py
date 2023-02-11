from typing import Union
from fastapi import FastAPI
from models.item_model import Item

#creacion de una aplicacion FastAPI:
app = FastAPI()

@app.get("/")
def read_root():
    return {"Hola": "Mundo"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q : Union[str, None] = None):
    return {"itemd_id": item_id, "q": q}

@app.put('/items/{item_id}')
def update_item(item_id: int, item: Item):
    return {'item_name': item.name, 'item_id': item_id, 'item_price': item.price}

