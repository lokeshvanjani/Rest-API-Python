import sqlite3

myconnection = sqlite3.connect('thisismydb.db')
mycursor = myconnection.cursor()
selectquery = "select * from users"
mydata = mycursor.execute(selectquery).fetchall()
for i in mydata:
    print(i)
myconnection.close()