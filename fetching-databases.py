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

# showing all databases
cursor.execute("SHOW DATABASES")


# 'fetchall()' method fetches all the rows from the last executed statement
databases = cursor.fetchall()  # it returns a list of all databases

# printing the list of databases
print(databases)

# showing one by one database
for database in databases:
    print(database)

