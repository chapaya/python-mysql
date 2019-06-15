import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="1234free",
  database="eran"
)
print(mydb)

cursor = mydb.cursor()

## defining the Query
query = "SELECT * FROM customer"

## getting records from the table
cursor.execute(query)

## fetching all records from the 'cursor' object
records = cursor.fetchall()

## Showing the data
for record in records:
    print(record)