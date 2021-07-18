import sqlite3

def selectOperations():

connection = sqlite3.connect("chinook.db")

def joinOperations():
  connection = sqlite3.connect("chinook.db")

cursor = connection.execute("""select albums.Tıtle,artists.Name from artists inner join albums on artists.ArtistId = albums.ArtistId""")

for row in cursor:
  print("Title :" +row[0] +"Name:" +row[1])
  
connection.close()

joinOperations()