import mysql.connector
from mysql.connector import Error

def insertData(id, name, address, telp, email):
    try:
        conn = mysql.connector.connect(host='localhost',
                                             database='testdb',
                                             user='test_user',
                                             password='Test_user!@#')
        cursor = conn.cursor()
        query = ("INSERT INTO customers (id, name, address, telp, email) "
                                "VALUES (%s, %s, %s, %s, %s)")

        column = (id, name, address, telp, email)
        cursor.execute(query, column)
        conn.commit()
        print("Data berhasil di-insert")

    except mysql.connector.Error as error:
        print("Gagal insert data ke table {}".format(error))

    finally:
        if (conn.is_connected()):
            cursor.close()
            conn.close()
            print("Connection ke MySQL disconnect")

insertData(7, 'Cacha', 'Bogor Raya', '777666333', 'cacha@nice.com')
insertData(8, 'Dadidu', 'Malang Raya', '333111222', 'dadidu@smart.com')
insertData(9, 'Endo', 'Jogja', '123321213', 'endo@coolman.com')
