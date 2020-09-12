import mysql.connector
from mysql.connector import Error

try:
    connection = mysql.connector.connect(host='localhost', database='testdb',
                                         user='test_user', password='Test_user!@#')
    cursor = connection.cursor()
    print("BEFORE UPDATE: ")
    query1 = ("select * from customers where id = 9")
    cursor.execute(query1)
    record = cursor.fetchone()
    print(record)

    query2 = ("update customers set telp = '9999999999' where id = 9")
    cursor.execute(query2)
    connection.commit()
    print("Update data berhasil  ")

    print("AFTER UPDATE: ")
    cursor.execute(query1)
    record = cursor.fetchone()
    print(record)

except mysql.connector.Error as error:
    print("Gagal update table: {}".format(error))
finally:
    if (connection.is_connected()):
        connection.close()
        print("Disconnect dari MySQL server")
