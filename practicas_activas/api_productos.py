#NOTA IMPORTANTE DEL PROGRAMA
#Los datos de los productos no se guardaran en un repositorio persistente.
#Solo se mantendran temporalmente almacenaos en la memoria de trabajo (RAM)

from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel

class productos(BaseModel):
    id: Optional[str]
    nombre: str
    precio_compra: float
    precio_venta: float
    proveedor: str

app = FastAPI()

productos = []

@app.get('/')
def index():
    return {'mensaje': 'Bienvenidos a la API de Productos'}

