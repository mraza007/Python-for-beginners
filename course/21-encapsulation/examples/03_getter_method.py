"""A getter gives safe, read-only access to private data.

Run me:  python 03_getter_method.py
"""

class Account:
    def __init__(self):
        self.__balance = 0

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:   # can't overdraw
            self.__balance -= amount

    def get_balance(self):                 # getter: read without overwriting
        return self.__balance

acc = Account()
acc.deposit(100)
acc.withdraw(30)
acc.withdraw(1000)        # ignored — not enough funds
print(acc.get_balance())  # 70
