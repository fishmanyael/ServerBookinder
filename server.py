import flask
import mysql.connector
import sys
import json

from database import bookinder_db

app = flask.Flask(__name__)

@app.route('/', methods = ['GET', 'POST'])
def chat():
    msg_received = flask.request.get_json()
    msg_subject = msg_received["subject"]

    if msg_subject == "register":
        return register(msg_received)
    elif msg_subject == "login":
        return login(msg_received)
    else:
        return "Invalid request."

def register(msg_received):
    name = msg_received["name"]
    email = msg_received["email"]
    password = msg_received["password"]
    phone = msg_received["phone"]
    age = msg_received["age"]

    select_query = "SELECT * FROM users where email = " + "'" + email + "'"
    db_cursor.execute(select_query)
    records = db_cursor.fetchall()
    if len(records) != 0:
        return "Another user used this email. Please chose another email."

    insert_query = "INSERT INTO users (name, password, email, age,phone_number) VALUES (%s, MD5(%s), %s, %s,%s)"
    insert_values = (name, password, email, age,phone)
    try:
        db_cursor.execute(insert_query, insert_values)
        bookinder_db.commit()
        return "success"
    except Exception as e:
        print("Error while inserting the new record :", repr(e))
        return "failure"

def login(msg_received):
    email = msg_received["username"]
    password = msg_received["password"]

    select_query = "SELECT email FROM users where email = " + "'" + email + "' and password = " + "MD5('" + password + "')"
    db_cursor.execute(select_query)
    records = db_cursor.fetchall()

    if len(records) == 0:
        return "failure"
    else:
        return "success"
try:
    bookinder_db = mysql.connector.connect(host="localhost", user="root", passwd="toor", database="bookinder_db")
except:
    sys.exit("Error connecting to the database. Please check your inputs.")
db_cursor = bookinder_db.cursor()
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True, threaded=True)
