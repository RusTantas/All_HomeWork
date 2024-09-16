'''

Задача "Средний баланс пользователя":
Для решения этой задачи вам понадобится решение предыдущей.
Для решения необходимо дополнить существующий код:
Удалите из базы данных not_telegram.db запись с id = 6.
Подсчитать общее количество записей.
Посчитать сумму всех балансов.
Вывести в консоль средний баланс всех пользователя.


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

# Удалите из базы данных not_telegram.db запись с id = 6.
# cursor.execute("DELETE FROM Users  WHERE id = ?", ( 6,))

# # Подсчитать общее количество записей.
# cursor.execute("SELECT COUNT(*) FROM Users")
# total1= cursor.fetchone()[0]
# print(total1)

# Посчитать сумму всех балансов.
# cursor.execute("SELECT SUM(balance) FROM Users")
# total1= cursor.fetchone()[0]
# print(total1)

# Вывести в консоль средний баланс всех пользователя.
cursor.execute("SELECT SUM(balance) FROM Users")
total1= cursor.fetchone()[0]
cursor.execute("SELECT COUNT(*) FROM Users")
total2= cursor.fetchone()[0]
print(total1/total2)

# Второй Вариант  Вывести в консоль средний баланс всех пользователя.
# cursor.execute("SELECT AVG(balance) FROM Users")
# total1= cursor.fetchone()[0]
# print(total1)



connection.commit()
connection.close()