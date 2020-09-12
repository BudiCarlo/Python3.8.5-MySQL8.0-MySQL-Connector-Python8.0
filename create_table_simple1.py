import mysql.connector

conn = mysql.connector.connect(
  host="localhost",
  user="test_user",
  password="Test_user!@#",
  database="testdb"
)

cursor = conn.cursor()
query = ("CREATE TABLE test_table (id INT(9), name VARCHAR(100), "
        " address VARCHAR(255), telp VARCHAR(30), email VARCHAR(100))")

cursor.execute(query)
print("Create table berhasil")

cursor.close()
conn.close()
