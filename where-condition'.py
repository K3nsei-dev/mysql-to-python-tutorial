import mysql.connector as mysql

db = mysql.connect(
    host='localhost',
    user='lifechoices',
    passwd='@Lifechoices1234',
    database='datacamp'
)

cursor = db.cursor()

# defining the Query
query = "SELECT * FROM users WHERE id = 5"

# getting the records from the table
cursor.execute(query)

# fetching all records
records = cursor.fetchall()

# showing the data
for records in records:
    print(records)
