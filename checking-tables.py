import mysql.connector as mysql

db = mysql.connect(
    host="localhost",
    user="lifechoices",
    passwd="@Lifechoices1234",
    database="datacamp"
)

cursor = db.cursor()

# 'DESC' table_name is used to get al the columns information
cursor.execute("DESC users")

# it will print all the columns as 'tuples' in a list
print(cursor.fetchall())
