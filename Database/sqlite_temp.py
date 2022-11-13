import sqlite3

db_list = ['Database/recipient.db', 'Database/products.db']
db_create = ['CREATE TABLE recipient (company_id INTEGER PRIMARY KEY, company_name TEXT, name TEXT, street TEXT, city TEXT)', 'CREATE TABLE products (id INTEGER PRIMARY KEY, product_name TEXT, product_price REAL)']

for (db, execute) in zip(db_list, db_create):
    conn = sqlite3.connect(db)
    c = conn.cursor()
    c.execute(execute)
    conn.commit
    conn.close