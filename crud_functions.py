import sqlite3

def initiate_db(db):
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

    # for i in range(4):
    #     cursor.execute('INSERT INTO Products (id, title, description, price) VALUES(?, ?, ?, ?)',
    #                (f'{i+1}', f'Продукт {i+1}', f'Описание {i+1}', f'{(i+1) * 100}'))

    conn.commit()
    conn.close()

def get_all_products(db):
    conn = sqlite3.connect(db)
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM Products')
    return cursor.fetchall()
    conn.close()


