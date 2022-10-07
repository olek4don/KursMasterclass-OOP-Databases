import sqlite3
import datetime
import pytz

db = sqlite3.connect("accounts.db")
db.execute("CREATE TABLE IF NOT EXISTS accounts (name TEXT PRIMARY KEY NOT NULL, balance INTEGER NOT NULL)")
db.execute("CREATE TABLE IF NOT EXISTS history (time TIMESTAMP NOT NULL,"
           " account TEXT NOT NULL, amount INTEGER NOT NULL, PRIMARY KEY (time, account))")

           
class Account(object):
    
    # @staticmethod
    def _current_time():
        return pytz.utc.localize(datetime.datetime.utcnow())
    
    def __init__(self, name: str, opening_balance: int = 0):
        cursor = db.execute("SELECT  name, balance FROM accounts WHERE (name = ?)", (name,))
        row = cursor.fetchone()
        
        if row:     # or if row is not None:
            self.name, self._balance = row
            print(f"Retrieved record for {self.name}. ", end='')
        else:
            self.name = name
            self._balance = opening_balance
            cursor.execute("INSERT INTO accounts VALUES(?, ?)", (name, opening_balance))
            cursor.connection.commit()
            print(f"Account created for {self.name}", end='')
        self.show_balance()

    def _save_update(self, amount):
        new_balance = self._balance + amount
        deposit_time = Account._current_time()
        db.execute("UPDATE accounts SET balance = ? WHERE (name = ?)", (new_balance, self.name))
        db.execute("INSERT INTO history VALUES (?, ?, ?)", (deposit_time, self.name, amount))
        db.commit()
        self._balance = new_balance


    def deposit(self, amount: int) -> float:
        if amount > 0.0:
            # new_balance = self._balance + amount
            # deposit_time = Account._current_time()
            # db.execute("UPDATE accounts SET balance = ? WHERE (name = ?)", (new_balance, self.name))
            # db.execute("INSERT INTO history VALUES (?, ?, ?)", (deposit_time, self.name, amount))
            # db.commit()
            # self._balance = new_balance
            self._save_update(amount)
            print(f"{amount / 100:.2f} deposited")
        return self._balance / 100

    def withdraw(self, amount: int) -> float:
        if 0 < amount <= self._balance:
#             new_balance = self._balance - amount
#             withdrawal_time = Account._current_time()
#             db.execute("UPDATE accounts SET balance = ? WHERE (name = ?", (new_balance, self.name))
#             db.execute("INSERT INTO history VALUES(?, ?, ?", (withdrawal_time, self.name, -amount))
#             db.commit()
#             self._balance = new_balance
            self._save_update(-amount)
            print(f"{amount / 100:.2f} withdraw")
            return amount / 100
        else:
            print("The amount must be greater than zero and no more than your account balance")
            return 0.0

    def show_balance(self):
        print(f"Balance on account {self.name} is {self._balance / 100:.2f}")


if __name__ == '__main__':
    john = Account("John")
    john.deposit(1010)
    john.deposit(10)
    john.deposit(10)
    john.deposit(30)
    john.withdraw(30)
    john.withdraw(0)
    john.show_balance()
    
    terry = Account("TerryJ")
    graham = Account("Graham", 9000)
    eric = Account("Eric", 7000)
    michael = Account("Michael")
    terryG = Account("TerryG")
       
    db.close()
