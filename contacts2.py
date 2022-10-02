import sqlite3

db =sqlite3.connect("contacts.sqlite")

new_email = "newemail@update.com"
phone = input("Please enter the phone number ")

# update_sql = f"UPDATE contacts SET email = '{new_email}' WHERE phone = {phone}"
update_sql = f"UPDATE contacts SET email = ? WHERE phone = ?"
print(update_sql)

update_cursor = db.cursor()
update_cursor.execute(update_sql, (new_email, phone))
print(f"{update_cursor.rowcount} rows updated")

print()
print(f"Are connections the same: {update_cursor.connection == db}")
print()

update_cursor.connection.commit()
update_cursor.close()

# for row in db.execute("SELECT * FROM contacts"):
    # print(row)

for name, phone, email in db.execute("SELECT * FROM contacts"):
    print(name)
    print(phone)
    print(email)
    print("-" * 20)

db.close() 
