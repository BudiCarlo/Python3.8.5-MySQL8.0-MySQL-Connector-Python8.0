import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="test_user",
  password="Test_user!@#"
)

mycursor = mydb.cursor()
mycursor.execute("CREATE DATABASE test_create_db")