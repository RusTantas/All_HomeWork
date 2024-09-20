import sqlite3
from random import random
import random
from urllib.parse import uses_query

connection = sqlite3.connect(database="database_r.db")
cursor = connection.cursor()

def initiate_db():
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Products (
    id INTEGER PRIMARY KEY,
    title TEXT,
    description TEXT,
    price INT
    );
    ''')


def get_all_products():
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




