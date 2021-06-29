import mysql.connector as mysql

db = mysql.connect(
    host='localhost',
    user='lifechoices',
    passwd='@Lifechoices1234',
    database='datacamp'
)

cursor = db.cursor()

# defining the query
query = "SELECT name, user_name FROM users"

# getting 'name', 'user_name' columns from the table
cursor.execute(query)

# fetching all records from the 'cursor' object
data = cursor.fetchall()

# showing the data
for pair in data:
    print(pair)
