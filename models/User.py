from pydantic import BaseModel

class User(BaseModel):
    username: str
    password: str
    name: str
    last_name: str
    email: str
    

class UserOut(BaseModel):
    name: str
    last_name: str
