import sqlite3

connection = sqlite3.connect('database.db')


with open('test.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

cur.execute("INSERT INTO menu (food_name, description,price) VALUES (?, ?, ?)",
            ('California Roll', 'Freshh',2)
            )

cur.execute("INSERT INTO menu (food_name, description,price) VALUES (?, ?, ?)",
            ('Pizza', 'Customizable 14 inch pizza',14)
            )

connection.commit()
connection.close()