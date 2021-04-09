import sqlite3

myconnection = sqlite3.connect('thisismydb.db')
mycursor = myconnection.cursor()
createtablequery = "create table if not exists users (id INTEGER PRIMARY KEY, username string, password string)"
mycursor.execute(createtablequery)
myusers = [
    (1, 'John', 'thisismypassword'),
    (2, 'Bob', 'qwerty'),
    (3, 'Coolguy', 'poiuyt')
]
insertdataquery = "insert into users values (?,?,?)"
mycursor.executemany(insertdataquery, myusers)

createstorequery = "create table if not exists stores (storeId INTEGER PRIMARY KEY, name string)"
mycursor.execute(createstorequery)
mystores = [
    (1, "Kalkaji"),
    (2, "CP"),
    (3, "Noida")
]
insertstorequery = "insert into stores values (?,?)"
mycursor.executemany(insertstorequery, mystores)

createitemsquery = "create table if not exists items (id INTEGER PRIMARY KEY, name string, price float, storeid integer, FOREIGN KEY(storeid) REFERENCES stores(storeId))"
mycursor.execute(createitemsquery)
items = [
    (1, 'Butter', 23.55, 2),
    (2, 'Honey', 19.42, 2),
    (3, 'Bread', 9.25, 3)
]
insertitemsquery = "insert into items values (?,?,?,?)"
mycursor.executemany(insertitemsquery, items)

myconnection.commit()
myconnection.close()

