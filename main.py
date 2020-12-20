from db.user_db import get_user, set_user, get_users, update_user, delete_user
from db.customer_db import get_customer, set_customer, get_customers, update_customer, delete_customer
from fastapi.middleware.cors import CORSMiddleware

from fastapi import FastAPI
from models.User import User
from models.Customer import Customer

api = FastAPI()

api.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@api.get("/usuario/{username}")
def getUser(username: str):
    return get_user(username)


@api.get("/usuario/todos/")
def usersGetAll():
    return get_users()


@api.put("/usuario/actualizar")
def usersUpdate(dataUpdate: dict):
    try:
        userUpdate = User(**{"username": dataUpdate["username"],
                             "password": dataUpdate["password"],
                             "name": dataUpdate["name"],
                             "last_name": dataUpdate["last_name"],
                             "email": dataUpdate["email"]
                             })
        response = {"res": "usuario actualizado",
                    "data": update_user(userUpdate)}
        return response
    except:
        return "se presento error"


@api.post("/usuario/crear")
def saveuser(user: dict):
    try:
        usercreate = User(**{"username": user["username"],
                             "password": user["password"],
                             "name": user["name"],
                             "last_name": user["last_name"],
                             "email": user["email"]
                             })
        result = set_user(usercreate)
        res = {
            'tipo': "ok",
            'msg': 'se creo el usuario',
            'data': result,
        }
        return res
    except:
        res = {
            'res': None,
            'msg': 'no se creo el usuario'
        }
        return res


@api.delete("/usuario/eliminar/{username}")
def deleteuser(user: str):
    try:
        result = delete_user(user)
        res = {
            'res': True,
            'msg': 'se elimino el usuario',
            'data': result,
        }
        return res
    except:
        res = {
            'res': False,
            'msg': 'no se elimino el usuario'
        }
        return res
# Customers
@api.get("/customer/{codigo}")
def getcustomer(codigo: str):
    return get_customer(codigo)


@api.get("/customer/todos/")
def customers_get_all():
    return get_customers()


@api.put("/customer/actualizar")
def customerupdate(dataupdate: dict):
    try:
        customerupdate = Customer(**{"codigo": dataupdate["codigo"],
                             "documento": dataupdate["documento"],
                             "name": dataupdate["name"],
                             "last_name": dataupdate["last_name"],
                             "email": dataupdate["email"],
                             "fecha": dataupdate["fecha"],
                            "direccion": dataupdate["direccion"],
                            "telefono": dataupdate["telefono"],
                            "celular": dataupdate["celular"],
                            "genero": dataupdate["genero"],
                             })
        response = {"res": "Cliente actualizado",
                    "data": update_customer(customerupdate)}
        return response
    except:
        return "se presento error"


@api.post("/customer/crear")
def savecustomer(customer: dict):
    try:
        customercreate = Customer(**{"codigo": customer["codigo"],
                             "documento": customer["documento"],
                             "name": customer["name"],
                             "last_name": customer["last_name"],
                             "email": customer["email"],
                             "fecha": customer["fecha"],
                            "direccion": customer["direccion"],
                            "telefono": customer["telefono"],
                            "celular": customer["celular"],
                            "genero": customer["genero"],
                             })
        result = set_customer(customercreate)
        res = {
            'tipo': "ok",
            'msg': 'se creo el cliente',
            'data': result,
        }
        return res
    except:
        res = {
            'res': None,
            'msg': 'no se creo el cliente'
        }
        return res


@api.delete("/customer/eliminar/{codigo}")
def deletecustomer(customer: str):
    try:
        result = delete_customer(customer)
        res = {
            'res': True,
            'msg': 'se elimino el cliente',
            'data': result,
        }
        return res
    except:
        res = {
            'res': False,
            'msg': 'no se elimino el cliente'
        }
        return res