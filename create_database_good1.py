import mysql.connector
from mysql.connector import Error

try:
    conn = mysql.connector.connect(host='localhost',
                                   database='testdb',
                                   user='test_user',
                                   password='Test_user!@#')

    query = ("CREATE DATABASE test_create_db")

    cursor = conn.cursor()
    result = cursor.execute(query)
    print("Database test_create_db berhasil di-create ")

except mysql.connector.Error as error:
    print("Gagal create database: {}".format(error))
finally:
    if (conn.is_connected()):
        cursor.close()
        conn.close()
        print("Connction ke MySQL di-disconnect")
