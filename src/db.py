import mysql.connector as mysql
from dotenv import load_dotenv
import os

load_dotenv()


mydb = mysql.connect(
    host=os.environ.get('host'),
    user=os.environ.get('name'),
    password=os.environ.get('password'),
    database=os.environ.get('database')
)

conn = mydb.cursor()

conn.execute("CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255))")


conn.execute("SHOW TABLES")

for table in conn:
    print(table)

sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
val = [
    ("Jamessss", "Street 123"),
    ("Jamesssss", "Street 321"),
    ("Jamessssss", "Street 3123"),
]

conn.executemany(sql, val)

mydb.commit()


print(conn.rowcount)


conn.execute("SELECT * FROM customers")

data = conn.fetchall()
data = conn.fetchone()

print(data)
for row in data:
    with open('data.txt', 'a') as f:
        row_data = "name: {}, address: {} \n".format(row[0], row[1])
        f.write(row_data)

