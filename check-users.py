import mysql.connector as mysql

db = mysql.connect(
    host='localhost',
    user='lifechoices',
    passwd='@Lifechoices1234',
    database='datacamp'
)

cursor = db.cursor()

# defining the Query
query = "SELECT * FROM users"

# getting records from the table
cursor.execute(query)

# fetching all records from the cursor object
records = cursor.fetchall()

# showing the data
for record in records:
    print(record)
