from pydantic import BaseModel

class Customer(BaseModel):
    codigo: str
    documento: str
    name: str
    last_name: str
    email: str
    fecha: str
    direccion: str
    telefono: str
    celular: str
    genero: str
    

class CustomerOut(BaseModel):
    name: str
    last_name: str
