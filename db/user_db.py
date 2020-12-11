from typing import  Dict
from pydantic import BaseModel



database_users = Dict[str, User]


class User(BaseModel):
    username: str
    password: str
    name: str
    last_name: str
    email: str
    
    



database_users = {
    "pperezl": User(**{"username":"pperezl",
                            "password":"1234",
                            "name":"Pepito",
                            "last_name":"Perez",
                            "email":"peperez@hotmail.com",}),

    "majo39": User(**{"username":"majo39",
                            "password":"LuciOP",
                            "name":"Maria",
                            "last_name":"Martinez",
                            "email":"majo39@gmail.com",}),

    "natsuki": User(**{"username":"natsuki",
                            "password":"gg962",
                            "name":"Angie",
                            "last_name":"Lopez",
                            "email":"alopez@hotmail.com",}),

    "capitan7": User(**{"username":"capitan7",
                            "password":"RocKo24",
                            "name":"Nelzon",
                            "last_name":"Diaz",
                            "email":"neld333@gmail.com",}),

    "sakura15": User(**{"username":"sakura15",
                            "password":"racoon",
                            "name":"Sebastian",
                            "last_name":"Rocero",
                            "email":"sroce@hotmail.com",}),

    "sario78": User(**{"username":"sario78",
                            "password":"lhoa",
                            "name":"Ivan",
                            "last_name":"Castiblanco",
                            "email":"ampresario2266@hotmail.com",}),
    "avilix": User(**{"username":"avilix",
                            "password":"glhf20",
                            "name":"Karen",
                            "last_name":"Cardenas",
                            "email":"avilixmei@hotmail.com",}),                                                                                                                        
}

def get_user(username: str):
    if username in database_users.keys():
        return database_users[username]
    else: 
        return None
    
def set_user(user_in_db: User):
    database_users[user_in_db.username] = user_in_db
    return user_in_db



