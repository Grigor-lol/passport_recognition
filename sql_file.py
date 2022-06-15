import mysql.connector
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="пкшырфыйд007",
    database = "passport"
)
print(mydb)
mycursor = mydb.cursor()
mycursor.execute('CREATE TABLE people(name VARCHAR(255), surname VARCHAR(255), patronymic VARCHAR(255))')
