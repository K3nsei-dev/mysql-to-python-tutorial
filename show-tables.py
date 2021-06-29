import mysql.connector as mysql

db = mysql.connect(
    host='localhost',
    user='lifechoices',
    passwd='@Lifechoices1234',
    database='datacamp'
)

cursor = db.cursor()

# getting all the tables which are present in 'datacamp' database
cursor.execute("SHOW TABLES")

tables = cursor.fetchall()  # returns list of tables present in the database

# showing all the tables one by one
for table in tables:
    print(table)
