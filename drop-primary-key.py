import mysql.connector as mysql

db = mysql.connect(
    host="localhost",
    user="lifechoices",
    passwd="@Lifechoices1234",
    database="datacamp"
)

cursor = db.cursor()

# dropping the 'id' column
cursor.execute("ALTER TABLE users DROP id")

# used to show table
cursor.execute("DESC users")

print(cursor.fetchall())
