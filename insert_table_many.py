import mysql.connector
from mysql.connector import Error

try:
    conn = mysql.connector.connect(host='localhost',
                                         database='testdb',
                                         user='test_user',
                                         password='Test_user!@#')

    query = """INSERT INTO customers (id, name, address, telp, email) 
                           VALUES (%s, %s, %s, %s, %s) """

    data = [(4, 'Fillipo Inzagi', 'Italy', '777777777', 'inzagi@italy.com'),
             (5, 'Ghana Brown', 'Ghana', '888888888', 'ghana@brown.com'),
             (6, 'Iniesta', 'Spanyol', '999999999', 'Iniesta@spain.com')]

    cursor = conn.cursor()
    cursor.executemany(query, data)
    conn.commit()
    print(cursor.rowcount, "row berhasil di-insert")

except mysql.connector.Error as error:
    print("Gagal insert ke table {}".format(error))

finally:
    if (conn.is_connected()):
        cursor.close()
        conn.close()
        print("Close connection ke MySQL")
