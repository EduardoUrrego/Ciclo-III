# cuendo se cree el metodo update_user, remplazar por linea de abajo
from db.user_db import get_user, set_user, get_users, update_user
# from db.user_db import update_user, get_user
# from db.user_db import UserInDB

from fastapi import FastAPI
from models.User import User

api = FastAPI()


@api.get("/user/{username}")
def getUser(username: str):
    print(username)
    get_user(username)


@api.get("/users/")
def usersGetAll():
    return get_users()


@api.put("/users")
def usersUpdate(dataUpdate: dict):
    userUpdate = User(**{"username": dataUpdate["username"],
                         "password": dataUpdate["password"],
                         "name": dataUpdate["name"],
                         "last_name": dataUpdate["last_name"],
                         "email": dataUpdate["email"]
                         })
    update_user(userUpdate)


@api.post("/users")
def saveUser(user: User):
    set_user(user)


# # editar un usuario

# @api.put("/user/editar")
# async def make_edition(edition_in: User):

#     user_in_db = get_user(edition_in.username)

#     if user_in_db == None:
#         raise HTTPException(status_code=404,
#                             detail='El usuario no existe')

#     user_in_db.password = edition_in.password
#     user_in_db.email = edition_in.email
#     update_user(user_in_db)

#     edition_in_db = User(**edition_in.dict(),
#                          password=user_in_db.password)

#     edition_in_db = User(**edition_in.dict(),
#                          email=user_in_db.email)

#     edition_in_db = set_user(edition_in_db)

#     edition_out = UserOut(**edition_in_db.dict())

#     return edition_out
