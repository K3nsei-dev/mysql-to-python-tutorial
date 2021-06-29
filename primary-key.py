import mysql.connector as mysql


db = mysql.connect(
    host='localhost',
    user='lifechoices',
    passwd='@Lifechoices1234',
    database='datacamp'
)

cursor = db.cursor()


# first we have to 'drop' the table which has already been created to create it again with the 'PRIMARY'
# "DROP TABLE table_name" statement will drop the table from the database
cursor.execute("DROP TABLE users")


# creating the table again with the 'PRIMARY KEY'
cursor.execute("CREATE TABLE users (id INT(11) NOT NULL AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), user_name VARCHAR(255))")
