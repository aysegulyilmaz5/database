import sqlite3

def selectOperations():

connection = sqlite3.connect("chinook.db")

connection.close()

selectOperations()


def insertCustomer():
  connection = sqlite3.connect("chinook.db")
  connection.execute("""insert into customers (firstName,lastName,city)values('Aysegul','Yilmaz','Istanbul')""")
  connection.commit connection.close()

insertCustomer()