import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="RamuSQL#123kaka",
    database="mydatabase"
)

mycursor = mydb.cursor()

mycursor.execute(
    "CREATE TABLE score_card (user_id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255))")
