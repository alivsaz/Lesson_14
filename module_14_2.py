# Средний баланс пользователя

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


cursor.execute('DELETE FROM Users WHERE id = ?', (6,))
cursor.execute('SELECT COUNT(*) FROM Users')
total_users = cursor.fetchone()[0]
cursor.execute('SELECT SUM(balance) FROM Users')
all_balances = cursor.fetchone()[0]
print(all_balances / total_users)

db.commit()
db.close()