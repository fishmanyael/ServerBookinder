import sys
import numpy
import mysql.connector

try:
    bookinder_db = mysql.connector.connect(host="localhost", user="root", passwd="toor")
except:
    sys.exit("Error connecting to the database. Please check your inputs.")

db_cursor = bookinder_db.cursor()
#db_cursor.execute("CREATE DATABASE bookinder_db")
db_cursor.execute("USE bookinder_db")
db_cursor.execute("SHOW tables")
print(db_cursor.fetchall())
# Users Table
# try:
#     db_cursor.execute("CREATE TABLE users (id INT(11) NOT NULL AUTO_INCREMENT PRIMARY KEY,name VARCHAR(255) NOT NULL,password VARCHAR(32) NOT NULL,email VARCHAR(32) NOT NULL UNIQUE,age INT(3) NOT NULL,phone_number VARCHAR(32) NOT NULL)")
#     print("users table created successfully.")
# except mysql.connector.DatabaseError:
#     sys.exit("Error creating the table. Please check if it already exists.")

describe_query = "DESCRIBE users"
db_cursor.execute(describe_query)
records = db_cursor.fetchall()
print(records)