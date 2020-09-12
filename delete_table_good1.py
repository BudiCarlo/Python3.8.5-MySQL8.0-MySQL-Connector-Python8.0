import mysql.connector
from mysql.connector import Error

try:
    conn = mysql.connector.connect(host='localhost', database='testdb',
                                         user='test_user', password='Test_user!@#')

    cursor = conn.cursor()
    print("BEFORE DELETING")
    query1 = ("select * from customers where id = 8")
    cursor.execute(query1)
    record = cursor.fetchone()
    print(record)

    query2 = ("Delete from customers where id = 8")
    cursor.execute(query2)
    conn.commit()

    cursor.execute(query1)
    records = cursor.fetchall()
    if len(records) == 0:
        print("\nDelete data berhasil ")

except mysql.connector.Error as error:
    print("Gagal delete data dari table: {}".format(error))
finally:
    if (conn.is_connected()):
        cursor.close()
        conn.close()
        print("Disconnect dari MySQL Server")