# Connecting to the database

# Importing 'mysql.connector' as mysql for convenient
import mysql.connector as mysql

# connecting to the database using 'connect()' method
# it takes 3 required parameters = 'host', 'user', and 'passwd'
db = mysql.connect(
    host="localhost",
    user="lifechoices",
    passwd="@Lifechoices1234"
)

# creating an instance of 'cursor' class which is used to execute the 'SQL' statements in 'Python'
cursor = db.cursor()

# creating a database called 'datacamp'
# 'execute()' method is used to compile a 'SQL' statement
# below statement is used to create the 'datacamp' database
cursor.execute("CREATE DATABASE datacamp")


print(db)  # it will print a connection if everything is fine
