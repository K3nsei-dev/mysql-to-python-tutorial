import mysql.connector as mysql

db = mysql.connect(
    host='localhost',
    user='lifechoices',
    passwd='@Lifechoices1234',
    database='datacamp'
)


cursor = db.cursor()


# creating a table called 'users' in the 'datacamp' database
cursor.execute("CREATE TABLE users (name VARCHAR(255), username VARCHAR(255))")
