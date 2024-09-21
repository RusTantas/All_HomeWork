import sqlite3
from random import random
import random
from urllib.parse import uses_query

connection = sqlite3.connect(database="database_r.db")
cursor = connection.cursor()
connection_2 = sqlite3.connect(database="database_users.db")
cursor_2 = connection_2.cursor()

def initiate_db():
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Products (
    id INTEGER PRIMARY KEY,
    title TEXT,
    description TEXT,
    price INT
    );
    ''')
    cursor_2.execute( '''
    CREATE TABLE IF NOT EXISTS Users (
    id INTEGER PRIMARY KEY,
    username TEXT NOT NULL,
    email TEXT NOT NULL,
    age INTEGER NOT NULL,
    balance INTEGER NOT NULL
    );    '''
    )
    connection.commit()
    connection.close()
    connection_2.commit()
    connection_2.close()




def get_all_products():
    connection = sqlite3.connect(database="database_r.db")
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM Products ")
    name = cursor.fetchall()

    connection.commit()
    connection.close()
    return name



def make_maks(title, description, price):
    cursor = connection.cursor()

    cursor.execute("INSERT INTO Products (title, description, price) VALUES (?, ?, ?)", (f"{title}", f"{description}", f"{price}"))
    connection.commit()
    connection.close()

def add_user(username, email, age, balans):
    connection_2 = sqlite3.connect(database="database_users.db")
    cursor_2 = connection_2.cursor()
    check_user = cursor_2.execute("SELECT * FROM Users WHERE username=?", (username,))
    if check_user.fetchone() is None:
        cursor_2.execute(
                         "INSERT INTO Users (username, email, age, balance) VALUES (?, ?, ?, ?)", (username,email,age, balans)
        )
        a =True
    else: a =False
    connection_2.commit()
    connection_2.close()
    return a



