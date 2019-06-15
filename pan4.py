import mysql.connector
import yaml

with open('config.yml', 'r') as f:
    config = yaml.load(f, Loader=yaml.FullLoader)
    #config = yaml.load(f)

mydb = mysql.connector.connect(
    host = config["host"],
    user = config["user"],
    passwd = config["passwd"],
    database = config["database"]
)
print(mydb)

ids=[]

def run_select():
    '''
    run select on customer table
    :return:
    '''
    #All table
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

def run_select_sf(con):
    '''
    run select on customer table
    :return:
    '''
    #Print all table
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

    #print according to condition
    cursor = mydb.cursor()
    query = "SELECT ID FROM customer where industry_type = %s"
    cursor.execute(query , (con,) )
    #  fetching all records from the 'cursor' object
    records = cursor.fetchall()
    for record in records:
        print(record)
        x = str(record).replace('(','').replace(',','').replace(')','') # leave only the id (88,)
        ids.append(x)


def run_update_sf(ids,newvalue):
    '''
    run update on table according to oldvalue and newvalue
    :return:
    '''
    for id in ids:
        mycursor = mydb.cursor()
        sql = "UPDATE customer SET industry_type = %s WHERE id = %s"
        val = (newvalue, id)
        print(sql + str(val))
        mycursor.execute(sql, val)
        mydb.commit()
        print(mycursor.rowcount, "record(s) affected")


def main():
    print("Print select...")
    run_select_sf('BKK21')
    print(ids)
    print("The ids list : " + str(ids))
    if not ids:   # Check if list is empty
        print("There are NO ids in list")
    else:
        print("There are ids in list .. running update ...")
        run_update_sf(ids, 'KARMI') # BKK12 -> BKK13
    print("Print select...")
    run_select()



if __name__ == '__main__':
    main()