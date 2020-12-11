  
from db.user_db import UserInDB
from db.user_db import update_user, get_user

from fastapi import FastAPI
from models.user import User

api = FastAPI()


@api.post("/users")
def saveUser(user: User):
    Database.set_user(user)




# editar un usuario

@api.put("/user/editar")

async def make_edition(edition_in:User):

    user_in_db = get_user(edition_in.username)

    if user_in_db == None:
        raise HTTPException(status_code = 404, 
                            detail='El usuario no existe')


    user_in_db.password=edition_in.password
    user_in_db.email=edition_in.email
    update_user(user_in_db)


    edition_in_db = User(**edition_in.dict(),
                        password=user_in_db.password)

    edition_in_db = User(**edition_in.dict(),
                        email=user_in_db.email)


    edition_in_db = set_user(edition_in_db)

    edition_out = UserOut(**edition_in_db.dict())






    return edition_out   



