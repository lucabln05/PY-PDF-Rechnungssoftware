import sqlite3

conn = sqlite3.connect('Database/recipient.db')
c = conn.cursor()

c.execute('''CREATE TABLE recipient(
    company_id INTEGER PRIMARY KEY AUTOINCREMENT,
    company_name text,
    name text,
    street text,
    city text
    )''')


conn.commit
conn.close