from db.user_db import get_user, set_user, get_users, update_user, delete_user
# from db.user_db import update_user, get_user
# from db.user_db import UserInDB

from fastapi import FastAPI
from models.User import User

api = FastAPI()


@api.get("/user/{username}")
def getUser(username: str):
    return get_user(username)


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
    return "Update User ok"

@api.post("/users")
def saveuser(user: dict):
    usercreate = User(**{"username": user["username"],
                         "password": user["password"],
                         "name": user["name"],
                         "last_name": user["last_name"],
                         "email": user["email"]
                         })
    set_user(usercreate)
    return "Add User ok"

### Delete a User ###
@api.delete("/user/{user}")
def deleteuser(user: str):
    """ Delete a user by username"""
    return delete_user(user)

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
