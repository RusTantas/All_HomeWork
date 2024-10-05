
"""
Цель: научиться описывать и использовать Pydantic модель.

Задача "Модель пользователя":
Подготовка:
Используйте CRUD запросы из предыдущей задачи.
Создайте пустой список users = []
Создайте класс(модель) User, наследованный от BaseModel, который будет содержать следующие поля:
id - номер пользователя (int)
username - имя пользователя (str)
age - возраст пользователя (int)

Измените и дополните ранее описанные 4 CRUD запроса:
get запрос по маршруту '/users' теперь возвращает список users.
post запрос по маршруту '/user/{username}/{age}', теперь:
Добавляет в список users объект User.
id этого объекта будет на 1 больше, чем у последнего в списке users. Если список users пустой, то 1.
Все остальные параметры объекта User - переданные в функцию username и age соответственно.
В конце возвращает созданного пользователя.
put запрос по маршруту '/user/{user_id}/{username}/{age}' теперь:
Обновляет username и age пользователя, если пользователь с таким user_id есть в списке users и возвращает его.
В случае отсутствия пользователя выбрасывается исключение HTTPException с описанием "User was not found" и кодом 404.
delete запрос по маршруту '/user/{user_id}', теперь:
Удаляет пользователя, если пользователь с таким user_id есть в списке users и возвращает его.
В случае отсутствия пользователя выбрасывается исключение HTTPException с описанием "User was not found" и кодом 404.


"""

from fastapi import FastAPI, Path, Body , HTTPException
from pydantic import BaseModel
from typing import List, Type

app = FastAPI()

users = []

class User(BaseModel):
    id: int = None
    username: str = None
    age: int = None



@app.get("/")
async def welcome () -> dict:
    return {"message": "Главная страница для задание 16_3"}

@app.get("/users")
async def ferst_get () -> List[User]:
    return users


@app.get("/users/{user_id}")
async def ferst_get (user_id : int) -> User:
    try:
        return users[user_id]
    except IndexError:
        raise HTTPException(status_code = 404, detail ='User is not founded')


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
        raise HTTPException(status_code = 404, detail ='User is not founded')

@app.delete('/user/{user_id}')
async def ferst_del(user_id: int) -> str:
    try:
        users.pop(user_id-1)
        return f"User {user_id} is deleted"
    except IndexError:
        raise HTTPException(status_code = 404, detail ='User is not founded')
