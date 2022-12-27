import mysql.connector as sqltor
mycon=sqltor.connect(host="localhost",user="root",passwd="aryaman", database="test", )

if mycon.is_connected():
       print("successfully connected to library")
