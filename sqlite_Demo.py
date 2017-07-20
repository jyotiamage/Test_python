import sqlite3

db=sqlite3.connect(':memory:')
db=sqlite3.connect(r'D:\TEM-Tivoli Endpoint Manager\Test_Python\mydb')

cursor=db.cursor()
#cursor.execute('''Create table Users(id Integer primary key, name text, phone text, email text unique, password text)''')

name1="Jyoti"
phone1="12345"
email1="user@example.com"
password1="abc@123"

#cursor.execute('''insert into users(name,phone,email,password)values(?,?,?,?)''',(name1,phone1,email1,password1))
#print("User1 data inserted!!")

cursor.execute('''select * from users''')
user1=cursor.fetchone()
print(user1)

db.commit()
db.close()
