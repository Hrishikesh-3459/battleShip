import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="RamuSQL#123kaka",
    database="mydatabase"
)

mycursor = mydb.cursor()
