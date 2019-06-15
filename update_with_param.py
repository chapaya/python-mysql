import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="1234free",
    database="eran"
)
print(mydb)

def run_select():
    '''
    run select on customer table
    :return:
    '''
    cursor = mydb.cursor()
    ## defining the Query
    #query = "SELECT ID FROM customer where industry_type='BKK1'"
    query = "SELECT * FROM customer"
    ## getting records from the table
    cursor.execute(query)
    ## fetching all records from the 'cursor' object
    records = cursor.fetchall()
    ## Showing the data
    for record in records:
      print(record)

def run_insert():
    '''
    run insert on customer table
    :return:
    '''
    cursor = mydb.cursor()
    ## defining the Query
    query = "INSERT INTO customer (id, name, city, industry_type) VALUES (%s, %s, %s ,%s)"
    ## storing values in a variable
    values = ("44", "Eran", "Magdiel" , "ops")
    ## executing the query with values
    cursor.execute(query, values)
    ## to make final output we have to run the 'commit()' method of the database object
    mydb.commit()
    print(cursor.rowcount, "record inserted")

def run_update():
    '''
    run insert on customer table
    :return:
    '''
    cursor = mydb.cursor()
    ## defining the Query
    sql = "UPDATE customer SET industry_type = 'BKK3' WHERE industry_type = 'BKK2'"
    cursor.execute(sql)
    ## to make final output we have to run the 'commit()' method of the database object
    mydb.commit()
    print(cursor.rowcount, "record updated")

def run_update_value(newvalue,oldvalue):
    '''
    run update on table according to oldvalue and newvalue
    :return:
    '''
    mycursor = mydb.cursor()
    sql = "UPDATE customer SET industry_type = %s WHERE industry_type = %s"
    val = (newvalue, oldvalue)
    #print(sql + str(val))
    mycursor.execute(sql, val)
    mydb.commit()
    print(mycursor.rowcount, "record(s) affected")


def main():
    print("Before update...")
    run_select()
    #run_insert()
    newvalue = 'BKK5'
    oldvalue = 'BKK4'
    run_update_value(newvalue,oldvalue)
    print("After update...")
    run_select()


if __name__ == '__main__':
    main()