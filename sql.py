import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="Ramukaka",
    database="mydatabase"
)

mycursor = mydb.cursor(buffered=True)
mycursor.execute("SELECT name FROM users")
myresult = mycursor.fetchall()
# print(myresult)
myres = []
for item in myresult:
    myres.append(item[0])

inp_name = input("Please enter winner's name: ")
if(inp_name not in myres):
    sql = "INSERT INTO users (name) VALUES (%s)"
    mycursor.execute(sql, (inp_name,))
    mydb.commit()
sql1 = "select name from users"
mycursor.execute(sql1)
res = mycursor.fetchall()
print(res)
