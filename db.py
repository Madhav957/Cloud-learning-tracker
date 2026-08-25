import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Madhav@2008",
    database="cloudflow"
)

print("MySQL connected successfully!")