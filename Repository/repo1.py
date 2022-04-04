import mysql.connector
from Models.ticket1 import BookTickets,RegUser,login




mydb = mysql.connector.connect(
    host='192.168.3.188',
    port='3306',
    user='training',
    password='training@123',
    db='training'
)
if mydb:
    print("Connected")
else:
    print("Not Connected")

my_cursor=mydb.cursor()

def getData():
    query=("SELECT * FROM person")
    my_cursor.execute(query)
    data=my_cursor.fetchall()
    return data

def insertData(ticket1:BookTickets):
    query="INSERT INTO person VALUES(%s,%s,%s)"
    values=(ticket1.id,ticket1.name,ticket1.amount)
    my_cursor.execute(query,values)
    mydb.commit()

def insertreg(x:RegUser):
    query1="INSERT INTO Registration VALUES(%s,%s)"
    values2=(x.username,x.PASSWORD)
    my_cursor.execute(query1,values2)
    mydb.commit()

def insetlogin(y:login):
    query2="INSERT INTO LOGIN VALUES(%s,%s)"
    values3=(y.userid,y.password)
    my_cursor.excecute(query2,values3)
    mydb.commit()