from pydantic import BaseModel

class User(BaseModel):
    id: int
    name: str
    surname: str
    age: int
    has_pet: bool

def createUser(id, name, surname, age, has_pet=False):
    return User(id = id, name=name , surname = surname , age = age, has_pet=has_pet)

user_list = [createUser(1, "Jose", "Lopez", 21, True),
             createUser(2, "Maria", "Rodriguez", 18, False),
             createUser(3, "Alejandro", "Martin", 55, True)]