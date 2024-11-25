# Первые пользователи

import sqlite3

db = sqlite3.connect('not_telegram.db')
cursor = db.cursor()

cursor.execute('CREATE TABLE IF NOT EXISTS Users '
               '(id INTEGER PRIMARY KEY, '
               'username TEXT IF NOT NULL, '
               'email TEXT IF NOT NULL, '
               'age INTEGER, '
               'balance INTEGER IF NOT NULL)')

for i in range(10):
    cursor.execute('INSERT INTO Users (username, email, age, balance) VALUES(?, ?, ?, ?)',
                   (f'User{i+1}', f'example{i+1}@gmail.com', f'{(i+1) * 10}', 1000))

for i in range(1, 11, 2):
    cursor.execute('UPDATE Users SET balance = ? WHERE id = ?',(500, i))

for i in range(1, 11, 3):
    cursor.execute('DELETE FROM Users WHERE id = ?', (i,))

cursor.execute('SELECT username, email, age, balance FROM Users WHERE age != 60')
users = cursor.fetchall()
for user in users:
    print(f'Имя:{user[0]} | Почта:{user[1]} | Возраст:{user[2]} | Баланс:{user[3]}')

db.commit()
db.close()