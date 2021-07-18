import sqlite3

def selectOperations():

connection = sqlite3.connect("chinook.db")

cursor = connection.execute("""select FirstName,LastName #from customers where city ='Prague'or city = 'Berlin' order #by FirstName""")

cursor = connection.execute("""select city,count(*) from Customers group by city""")

for row in cursor:
  print("First Name =" +row[1])

for row in cursor:
  print("City =" +row[0])
  print("Count ="+str(row[1]))
  print(*********)


connection.close()

selectOperations()





   










