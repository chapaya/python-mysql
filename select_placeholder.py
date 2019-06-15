import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="1234free",
    database="eran"
)
print(mydb)

cursor = mydb.cursor()

con = "BKK10"
query = 'SELECT name FROM workers WHERE symbol = %s '

query = "SELECT ID FROM customer where industry_type = %s"

# cursor.execute("SELECT name FROM workers WHERE symbol=%s", (con,))
# ## executing the query with values
#cursor.execute(query, ("BKK10",) )

cursor.execute(query, (con,) )

records = cursor.fetchall()
    ## Showing the data
for record in records:
    print(record)