from flask import Flask
from flask import render_template
import sqlite3
import mysql.connector

mydb = mysql.connector.connect(
  host="database-1.cxli1xpe8prx.us-east-1.rds.amazonaws.com",
  user="web_app",
  password="Password!",
  database="restaurant",
  auth_plugin="mysql_native_password"
)

print(mydb)

app = Flask(__name__)

# def get_db_connection():
#     conn = sqlite3.connect('database.db')
#     conn.row_factory = sqlite3.Row
#     return conn






@app.route('/')
def index():
    return render_template('./index.html')



@app.route('/menu')
def menu():
    conn = mydb.cursor()
    conn.execute('SELECT * FROM menu')
    menu = conn.fetchall()
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
    app.run(threaded=True, port=5000)