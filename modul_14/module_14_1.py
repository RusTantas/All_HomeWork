'''

Цель: освоить основные команды языка SQL и использовать их в коде используя SQLite3.

Задача "Первые пользователи":
Создайте файл базы данных not_telegram.db и подключитесь к ней, используя встроенную библиотеку sqlite3.
Создайте объект курсора и выполните следующие действия при помощи SQL запросов:
Создайте таблицу Users, если она ещё не создана. В этой таблице должны присутствовать следующие поля:
id - целое число, первичный ключ
username - текст (не пустой)
email - текст (не пустой)
age - целое число
balance - целое число (не пустой)
Заполните её 10 записями:
User1, example1@gmail.com, 10, 1000
User2, example2@gmail.com, 20, 1000
User3, example3@gmail.com, 30, 1000
...
User10, example10@gmail.com, 100, 1000
Обновите balance у каждой 2ой записи начиная с 1ой на 500:
User1, example1@gmail.com, 10, 500
User2, example2@gmail.com, 20, 1000
User3, example3@gmail.com, 30, 500
...
User10, example10@gmail.com, 100, 1000
Удалите каждую 3ую запись в таблице начиная с 1ой:
User2, example2@gmail.com, 20, 1000
User3, example3@gmail.com, 30, 500
User5, example5@gmail.com, 50, 500
...
User9, example9@gmail.com, 90, 500

Сделайте выборку всех записей при помощи fetchall(), где возраст не равен 60 и выведите их в консоль в следующем формате (без id):
Имя: <username> | Почта: <email> | Возраст: <age> | Баланс: <balance>

Пример результата выполнения программы:
Вывод на консоль:
Имя: User2 | Почта: example2@gmail.com | Возраст: 20 | Баланс: 1000
Имя: User3 | Почта: example3@gmail.com | Возраст: 30 | Баланс: 500
Имя: User5 | Почта: example5@gmail.com | Возраст: 50 | Баланс: 500
Имя: User8 | Почта: example8@gmail.com | Возраст: 80 | Баланс: 1000
Имя: User9 | Почта: example9@gmail.com | Возраст: 90 | Баланс: 500


'''


import sqlite3
from random import random
import random
from urllib.parse import uses_query

connection = sqlite3.connect(database="not_telegram.db")
cursor = connection.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS Users (
id INTEGER PRIMARY KEY,
username TEXT NOT NULL,
email TEXT NOT NULL,
age INTEGER,
balance INTEGER NOT NULL
)
''')
cursor.execute('CREATE INDEX IF NOT EXISTS idx_email ON Users (email)')

# Создание циклом базу данных
# for i in range(10):
#     cursor.execute("INSERT INTO Users (username, email, age, balance) VALUES (?, ?, ?, ?)", (f"User{i+1}", f"example{i+1}@gmail.com", (i+1) * 10, 1000  ))


# Обновите balance у каждой 2ой записи начиная с 1ой на 500:
# for i in range(11):
#     if i % 2 == 0:
#         cursor.execute("UPDATE Users SET balance = ? WHERE id = ?", (500, i))
#     else: pass


# Удалите каждую 3ую запись в таблице начиная с 1ой:
# for i in range(1, 11, 3):
#     cursor.execute("DELETE FROM Users  WHERE id = ?", ( i,))



# Сделайте выборку всех записей при помощи fetchall(), где возраст не равен 60 и выведите их в консоль
cursor.execute("SELECT username, email, age, balance FROM Users WHERE age > 60")

users = cursor.fetchall()
for user in users:
        print(user)

connection.commit()
connection.close()