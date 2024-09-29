from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def welcome () -> dict:
    return {"message": "Главная страница"}

@app.get("/user/admin")
async def admin () -> dict:
    return {"message": "Вы вошли как администратор"}

@app.get("/user/{user_id}")
async def user_id (user_id: int) -> dict:
    return {"message": f"Вы вошли как пользователь №{user_id}"}

@app.get("/user")
async def user_name (username: str,  age: int) :
    return { f"Информация о пользователею Имя: {username}, Возраст {age}."}


#http://127.0.0.1:8000/user?username=%27Ilya%27&age=24