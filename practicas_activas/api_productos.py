from fastapi import FastAPI

#NOTA IMPORTANTE DEL PROGRAMA
#Los datos de los productos no se guardaran en un repositorio persistente.
#Solo se mantendran temporalmente almacenaos en la memoria de trabajo (RAM)

app = FastAPI()

@app.get('/')
def index():
    return {'mensaje': 'Bienvenidos a la API de Productos'}

