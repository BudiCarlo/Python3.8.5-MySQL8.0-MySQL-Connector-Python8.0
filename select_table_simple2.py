import mysql.connector
from mysql.connector import Error

try:
    connection = mysql.connector.connect(host='localhost', database='testdb',
                                         user='test_user', password='Test_user!@#')

    query = "select * from customers"
    cursor = connection.cursor()
    cursor.execute(query)
    records = cursor.fetchall()
    spc = " "
    print("Jumlah rows di table customers: ", cursor.rowcount)

    print("-------------------------------------------------")
    print("ID       NAME     ADDRESS      TELP       EMAIL  ")
    print("--------------------------------------------==---")
    for row in records:
        print(row[0], row[1], row[2], row[3], row[4])
    print("-------------------------------------------==----")
except Error as e:
    print("Error fetch data", e)
finally:
    if (connection.is_connected()):
        connection.close()
        cursor.close()
        print("Connection ke MySQL di-disconnect")