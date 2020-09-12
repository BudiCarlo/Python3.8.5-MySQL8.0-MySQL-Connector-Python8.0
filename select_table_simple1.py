import mysql.connector
from mysql.connector import Error

try:
    connection = mysql.connector.connect(host='localhost', database='testdb',
                                         user='test_user', password='Test_user!@#')

    query = "select * from customers"
    cursor = connection.cursor()
    cursor.execute(query)
    records = cursor.fetchall()
    print("Jumlah rows di table customers: ", cursor.rowcount)

    print("\nPrint semua record (row)")
    print("--------------------------")
    for row in records:
        print("Id = ", row[0], )
        print("Name = ", row[1], )
        print("Address  = ", row[2], )
        print("Telp  = ", row[3], )
        print("Email = ", row[4], "\n")

except Error as e:
    print("Error fetch data", e)
finally:
    if (connection.is_connected()):
        connection.close()
        cursor.close()
        print("Connection ke MySQL di-disconnect")