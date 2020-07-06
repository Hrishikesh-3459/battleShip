import mysql.connector


class dbMysql():
    def __init__(self):
        self.pwd = "Ramukaka"
        self.username = "root"
        self.host = "localhost"
        self.database = "mydatabase"
        self.mydb = None

    def connection(self):
        self.mydb = mysql.connector.connect(
            host=self.host,
            user=self.username,
            passwd=self.pwd,
            database=self.database
        )
        return(self.mydb)

    def configure_db(self, mycursor):
        mycursor.execute("CREATE DATABASE IF NOT EXISTS mydatabase")
        self.mydb.commit()
        mycursor.execute(
            "CREATE TABLE IF NOT EXISTS users (user_id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255))")
        self.mydb.commit()
        mycursor.execute(
            "CREATE TABLE IF NOT EXISTS score_card (serial_no INT AUTO_INCREMENT, user_id int, name VARCHAR(255), score int, date_time TIMESTAMP, PRIMARY KEY (serial_no), FOREIGN KEY (user_id) REFERENCES users(user_id))")
        self.mydb.commit()
