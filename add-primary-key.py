import mysql.connector as mysql


db = mysql.connect(
    host='localhost',
    user='lifechoices',
    passwd='@Lifechoices1234',
    database='datacamp'
)

cursor = db.cursor()


# add 'id' column to the 'users' table
# 'FIRST' keyword in the statement will add a column in the starting of the table
cursor.execute("ALTER TABLE users ADD COLUMN id INT(11) NOT NULL AUTO_INCREMENT PRIMARY KEY FIRST")

cursor.execute("DESC users")


print(cursor.fetchall())
