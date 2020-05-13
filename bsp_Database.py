import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="Ramukaka",
    database="mydatabase"
)

mycursor = mydb.cursor()

mycursor.execute(
    "CREATE TABLE score_card (user_id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255))")

# CREATE TABLE score_card (serial_no INT AUTO_INCREMENT, user_id int, name VARCHAR(255), score int, date_time TIMESTAMP, PRIMARY KEY (serial_no), FOREIGN KEY (user_id) REFERENCES users(user_id));
