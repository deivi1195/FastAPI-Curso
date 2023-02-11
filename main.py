from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel

#creacion de una aplicacion FastAPI:
app = FastAPI()

class Item(BaseModel):
    name: str
    price: Float
    is_offer: Union[Bool, None] = None


@app.get("/")
def read_root():
    return {"Hola": "Mundo"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q : Union[str, None] = None):
    return {"itemd_id": item_id, "q": q}


