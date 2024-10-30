from fastapi import FastAPI
import user

app = FastAPI()

@app.get("/users")
async def getUserInfo():
    return user.user_list

@app.get("/users/{id}")
async def getUserInfo(id: int):
    return list(filter(lambda user: user.id == id, user.user_list))

