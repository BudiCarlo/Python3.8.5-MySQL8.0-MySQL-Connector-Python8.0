import mysql.connector
from mysql.connector import Error

try:
    conn = mysql.connector.connect(host='localhost',
                                         database='testdb',
                                         user='test_user',
                                         password='Test_user!@#')

    query = """CREATE TABLE customer ( 
            id INT(11) NOT NULL,
            Name VARCHAR(100) NOT NULL,
            address VARCHAR(255) NOT NULL,
            telp VARCHAR(20),
            email VARCHAR(100), 
            PRIMARY KEY (id))"""

    cursor = conn.cursor()
    result = cursor.execute(query)
    print("Table customers berhasil di-create ")

except mysql.connector.Error as error:
    print("Gagal create table customers: {}".format(error))
finally:
    if (conn.is_connected()):
        cursor.close()
        conn.close()
        print("Connction ke MySQL di-disconnect")
