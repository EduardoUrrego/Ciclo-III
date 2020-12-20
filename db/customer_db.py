from typing import Dict
from pydantic import BaseModel
from models.Customer import Customer

database_customers = Dict[str, Customer]


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


database_customers = {
    "2020001": Customer(**{"codigo": "pperezl",
                       "documento": "1234",
                       "name": "Pepito",
                       "last_name": "Perez",
                       "email": "peperez@hotmail.com",
                       "fecha": "1997-04-19",
                       "direccion": "cll 5 # 34 -  27, Bogota D.C",
                       "telefono": "6836699",
                       "celular": "3008764592",
                       "genero": "masculino",
                       }),

    "2020002": Customer(**{"codigo": "majo39",
                      "documento": "LuciOP",
                      "name": "Maria",
                      "last_name": "Martinez",
                      "email": "majo39@gmail.com",
                      "fecha": "1985-05-03",
                       "direccion": "cll 9 # 25 -  48, Medellin",
                       "telefono": "2618831",
                       "celular": "3107894564",
                       "genero": "femenino",
                       }),

    "2020003": Customer(**{"codigo": "natsuki",
                       "documento": "gg962",
                       "name": "Angie",
                       "last_name": "Lopez",
                       "email": "alopez@hotmail.com", 
                       "fecha": "1974-09-28",
                       "direccion": "cr 67b # 85 - 34, Bogota D.C",
                       "telefono": "5764359",
                       "celular": "3187650284",
                       "genero": "femenino",
                       }),
}


def get_customer(codigo: str):
    if codigo in database_customers.keys():
        return database_customers[codigo]
    else:
        return None


def get_customers():
    return database_customers


def set_customer(customer_in_db: Customer):
    database_customers[customer_in_db.codigo] = customer_in_db
    return customer_in_db


def update_customer(customerUpdate: Customer):
    print(database_customers[customerUpdate.codigo])
    database_customers[customerUpdate.codigo] = customerUpdate
    print(database_customers[customerUpdate.codigo])


def delete_customer(codigo: str):
    del database_customers[codigo]
    return database_customers
