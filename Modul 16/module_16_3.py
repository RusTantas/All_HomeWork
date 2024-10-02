'''
Задача "Имитация работы с БД":
Создайте новое приложение FastAPI и сделайте CRUD запросы.
Создайте словарь users = {'1': 'Имя: Example, возраст: 18'}
Реализуйте 4 CRUD запроса:
get запрос по маршруту '/users', который возвращает словарь users.
post запрос по маршруту '/user/{username}/{age}', который добавляет в словарь по максимальному по значению ключом значение строки "Имя: {username}, возраст: {age}". И возвращает строку "User <user_id> is registered".
put запрос по маршруту '/user/{user_id}/{username}/{age}', который обновляет значение из словаря users под ключом user_id на строку "Имя: {username}, возраст: {age}". И возвращает строку "The user <user_id> is registered"
delete запрос по маршруту '/user/{user_id}', который удаляет из словаря users по ключу user_id пару.
Выполните каждый из этих запросов по порядку. Ответы должны совпадать:
1. GET '/users'
{
"1": "Имя: Example, возраст: 18"
}
2. POST '/user/{username}/{age}' # username - UrbanUser, age - 24
"User 2 is registered"
3. POST '/user/{username}/{age}' # username - NewUser, age - 22
"User 3 is registered"
4. PUT '/user/{user_id}/{username}/{age}' # user_id - 1, username - UrbanProfi, age - 28
"User 1 has been updated"
5. DELETE '/user/{user_id}' # user_id - 2
"User 2 has been deleted"
6. GET '/users'
{
"1": "Имя: UrbanProfi, возраст: 28",
"3": "Имя: NewUser, возраст: 22"
}
'''



from fastapi import FastAPI, Path
from typing import  Annotated

app = FastAPI()

users = {'1': 'Имя: Example, возраст: 18'}



@app.get("/")
async def welcome () -> dict:
    return {"message": "Главная страница для задание 16_3"}

@app.get("/users")
async def ferst_get () -> dict:
    return users


@app.post('/user/{username}/{age}')
async def ferst_post(username: str, age: int) -> str:
    curent_index = str(int(max(users, key = int))+ 1)
    users[curent_index]= f'Имя: {username}, возраст: {age}'
    return f"User {curent_index } is registered"

@app.put('/user/{user_id}/{username}/{age}')
async def ferst_put(user_id: int, username: str, age: int) -> str:
    users[user_id]= f'Имя: {username}, возраст: {age}'
    return f"User {user_id } is registered"

@app.delete('/user/{user_id}')
async def ferst_del(user_id: int) -> str:
    users.pop(user_id)
    return f"User {user_id } is deleted"
