import mysql.connector

conn = mysql.connector.connect(
  host="localhost",
  user="test_user",
  password="Test_user!@#",
  database="testdb"
)

mycursor = conn.cursor()

mycursor.execute("INSERT INTO customers "
                  "(id, name, address, telp, email) "
                  "VALUES (2, 'abdul', 'Jakarta', '1234567', 'abdulmti@gmail.com')")
conn.commit()

print("Data berhasil di-insert")

mycursor.close()
conn.close()
