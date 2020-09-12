import mysql.connector
from mysql.connector import errorcode

try:
  conn = mysql.connector.connect(
    user='test_user',
    password='Test_user!@#1',
    host='localhost',
    database='testdb')
  print("Test connection ke database berhasil")
except mysql.connector.Error as err:
  if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
    print("User atau Password yang anda masukkan salah")
  elif err.errno == errorcode.ER_BAD_DB_ERROR:
    print("Database: testdb, tidak ditemukan")
  else:
    print(err)
else:
  conn.close()