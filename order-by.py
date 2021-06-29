import mysql.connector as mysql

db = mysql.connect(
    host='localhost',
    user='lifechoices',
    passwd='@Lifechoices1234',
    database='datacamp'
)

cursor = db.cursor()

# defining the Query (Ascending Order)
# query = "SELECT * FROM users ORDER BY name"

# defining the Query (Descending Order)
query = "SELECT * FROM users ORDER BY name DESC"


# getting records from the table
cursor.execute(query)

# fetching all records from the table
records = cursor.fetchall()

# showing the data
for record in records:
    print(record)
