import sqlite3
import pytz
# import datetime

db = sqlite3.connect("accounts.db", detect_types=sqlite3.PARSE_DECLTYPES)

for row in db.execute("SELECT * FROM localhistory"):

# for row in db.execute("SELECT strftime('%Y-%m-%d %H:%M:%f', history.time, 'localtime') AS localtime,"
                    #   " history.account, history.amount FROM history ORDER BY history.time"):
    print(row)
    # utc_time = row[0]
    # local_time = pytz.utc.localize(utc_time).astimezone()
    
    # local_time = datetime.datetime.strptime(row[0], '%Y-%m-%d %H:%M:%S.%f%z') # let us for return converted type
    # local_time = row[0]
    
    # print(f"{utc_time}\t{local_time}")

db.close()