from config import db   # файл с настройками
import sqlite3

def initiate_db():
    global db
    conn = sqlite3.connect(db)
    cursor = conn.cursor()
    cursor.execute(
    '''
    CREATE TABLE IF NOT EXISTS Products (
    id INTEGER PRIMARY KEY, 
    title TEXT NOT NULL, 
    description TEXT, 
    price INTEGER IF NOT NULL)
    '''
    )

    cursor.execute(
    '''
    CREATE TABLE IF NOT EXISTS Users (
    id INTEGER PRIMARY KEY, 
    username TEXT NOT NULL, 
    email TEXT NOT NULL,
    age INTEGER NOT NULL,
    balance INTEGER NOT NULL)
    '''
    )

    conn.commit()
    conn.close()

def get_all_products():
    global db
    conn = sqlite3.connect(db)
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM Products')
    return cursor.fetchall()
    conn.close()

def add_user(username, email, age):
    global db
    conn = sqlite3.connect(db)
    cursor = conn.cursor()
    cursor.execute('INSERT INTO Users (username, email, age, balance) VALUES(?, ?, ?, ?)',
                    (username, email, age, 1000))
    conn.commit()
    conn.close()

def is_included(username):
    global db
    conn = sqlite3.connect(db)
    cursor = conn.cursor()
    if cursor.execute('SELECT COUNT(*) FROM Users WHERE username = ?', (username,)).fetchone()[0]:
        conn.close()
        return True
    else:
        conn.close()
        return False
