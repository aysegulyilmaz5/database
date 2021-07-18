import sqlite3

def selectOperations():

connection = sqlite3.connect("chinook.db")


connection.close()

selectOperations()

def updateCustomer():
  connection = sqlite3.connect("chinook.db")
connection.execute("""update customers set city = 'Istanbul,where city = 'Ankara'""")

connection.commit()
connection.close()

updateCustomer()