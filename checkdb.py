import sqlite3

conn = sqlite3.connect("contacts.sqlite")

name = input("Enter your name for retrieve data: ")

for row in conn.execute("SELECT * FROM contacts WHERE name LIKE ?", (name,)):
    print(row)

conn.close()
