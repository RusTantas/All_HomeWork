from typing import List

from fastapi import FastAPI, HTTPException, Request, Form
from fastapi.openapi.utils import status_code_ranges
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
from starlette import status

# import sys
# sys.path.append('pythonProject\.venv\Lib')
# import jinja2


app = FastAPI()
templates = Jinja2Templates(directory="Urban/fastapi/templates")
users = []

class User(BaseModel):
    id: int = None
    username: str = None
    age: int = None

@app.get("/")
async def welcome (request : Request) -> HTMLResponse:
    return templates.TemplateResponse("users.html", {"request":request, "users": users})

# @app.get("/users")
# async def ferst_get_1 (request:Request) -> HTMLResponse:
#     return templates.TemplateResponse("users.html", {"request":request, "users": users})


@app.get(path="/users/{user_id}")
async def ferst_get (request:Request, user_id : int) -> HTMLResponse:
    try:
        return templates.TemplateResponse("users.html", {"request":request, "user": users[user_id-1]})
    except IndexError:
        raise HTTPException(status_code = 404, detail ='ID is not founded')


@app.post('/users/{username}/{age}')
async def ferst_post( username: str, age: int) -> User:
    user = User()
    if len(users) == 0:
         user.id = 1
    else:
        user.id = len(users) + 1
    user.username = username
    user.age = age
    users.append(user)
    return user


@app.put('/user/{user_id}/{username}/{age}')
async def ferst_put(user_id: int, username: str, age: int) -> str:
    try:
        user_edit = users[user_id-1]
        user_edit.username = username
        user_edit.age = age
        return f"User {user_id} is registered"
    except IndexError:
        raise HTTPException(status_code = 404, detail ='ID is not founded')

@app.delete('/user/{user_id}')
async def ferst_del(user_id: int) -> str:
    try:
        users.pop(user_id-1)
        return f"User {user_id} is deleted"
    except IndexError:
        raise HTTPException(status_code = 404, detail ='ID is not founded')




# http://127.0.0.1:8000/docs
#post запрос по маршруту '/user/{username}/{age}', который добавляет в словарь по максимальному по значению
# ключом значение строки "Имя: {username}, возраст: {age}". И возвращает строку "User <user_id> is registered".

# @app.post('/user/{username}/{age}')
# async def ferst_post(username: str, age: int) -> str:
#     curent_index = str(int(max(users, key = int))+ 1)
#     users[curent_index]= f'Имя: {username}, возраст: {age}'
#     return f"User {curent_index } is registered"
#
# @app.put('/user/{user_id}/{username}/{age}')
# async def ferst_put(user_id: int, username: str, age: int) -> str:
#     users[user_id]= f'Имя: {username}, возраст: {age}'
#     return f"User {user_id } is registered"
#
# @app.delete('/user/{user_id}')
# async def ferst_del(user_id: int) -> str:
#     users.pop(user_id)
#     return f"User {user_id } is deleted"

#
# @app.get("/user/admin")
# async def admin () -> dict:
#     return {"message": "Вы вошли как администратор"}
#
# @app.get("/user/{user_id}")
# async def user_id (user_id: Annotated[int, Path(ge=1, le=100, description='Enter User ID', example= '1' )]) -> dict:
#     return {"message": f"Вы вошли как пользователь №{user_id}"}
#
# @app.get("/user/{username}/{age}")
# async def user_name (username: Annotated[str, Path(min_length=5, max_length=20, description='Enter username', example='UrbanUser')],
#                      age: Annotated[int, Path(ge=18, le=120, description='Enter age', example= '24' )]) -> dict:
#     return { "message" :f"Информация о пользователею Имя: {username}, Возраст {age}."}


#http://127.0.0.1:8000/user?username=%27Ilya%27&age=24
#

