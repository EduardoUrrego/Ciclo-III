from db.user_db import get_user, set_user, get_users, update_user, delete_user
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI
from models.User import User

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
