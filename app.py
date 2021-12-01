from flask import Flask
from flask import render_template
import sqlite3
# import mysql.connector

# mydb = mysql.connector.connect(
#   host="localhost",
#   user="yourusername",
#   password="yourpassword",
#   database="mydatabase"
# )

# print(mydb)



def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn




app = Flask(__name__)

@app.route('/')
def index():
    return render_template('./index.html')



@app.route('/menu')
def menu():
    conn = get_db_connection()
    menu = conn.execute('SELECT * FROM menu').fetchall()
    print(menu)
    conn.close()
    return render_template('./menu.html', menu=menu)

@app.route('/reservation')
def reservation():
    return render_template('./reservation.html')

@app.route('/about_us')
def about_us():
    return render_template('./about_us.html')

if __name__ == "__main__":
    app.run()