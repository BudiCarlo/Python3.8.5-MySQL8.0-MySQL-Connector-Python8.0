import mysql.connector

conn = mysql.connector.connect(
    user='test_user', 
    password='Test_user!@#',
    host='127.0.0.1',
    database='testdb')

print("Berhasil connect ke database")
print(conn.database)
conn.close()