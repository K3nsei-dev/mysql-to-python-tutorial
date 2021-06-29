import mysql.connector as mysql

db = mysql.connect(
    host='localhost',
    user='lifechoices',
    passwd='@Lifechoices1234',
    database='datacamp'
)

cursor = db.cursor()

# defining the Query
query = "SELECT user_name FROM users"

# getting 'user_name' column from the table
cursor.execute(query)

# fetching all usernames from the 'cursor' object
usernames = cursor.fetchall()

# showing the data
for username in usernames:
    print(username)
