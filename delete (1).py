import sqlite3

def selectOperations():

connection = sqlite3.connect("chinook.db")


connection.close()

selectOperations()


def deleteCustomer():
  connection = sqlite3.connect("chinook.db")
  connection.execute("""delete from customers where customerid = 60""")

  connection.commit()
  connection.close()
deleteCustomer()