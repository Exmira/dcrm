# Install Mysql
# Pip install mysql 
# Pip install mysql-connector

import mysql.connector

dataBase = mysql.connector.connect(
  host = 'localhost',
  user = 'root',
  passwd = 'password123'
)

# PREPARE a cursor object

cursorObject = dataBase.cursor()

# Create a Database


cursorObject.execute("CREATE DATABASE mydb")
 
print("Database Created")