  
from fastapi import FastAPI
from models.user import User

api = FastAPI()


@api.post("/users")
def saveUser(user: User):
    Database.set_user(user)




