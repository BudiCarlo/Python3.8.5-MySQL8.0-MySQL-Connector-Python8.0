import mysql.connector
from mysql.connector import Error

try:
    conn = mysql.connector.connect(host='localhost',
                                   database='testdb',
                                   user='test_user',
                                   password='Test_user!@#')
    if conn.is_connected():
        db_info = conn.get_server_info()
        print("Connect ke MySQL Server versi ", db_info)
        cursor = conn.cursor()
        cursor.execute("select database();")
        record = cursor.fetchone()
        print("Berhasil connect ke database: ", record)

except Error as e:
    print("Error connect ke MySQL Server ", e)
finally:
    if (conn.is_connected()):
        cursor.close()
        conn.close()
        print("Close connection dari MySQL Server")
