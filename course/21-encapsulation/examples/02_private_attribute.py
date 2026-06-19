"""A private attribute (leading __) can only change through methods.

Run me:  python 02_private_attribute.py
"""

class Account:
    def __init__(self):
        self.__balance = 0           # private

    def deposit(self, amount):
        if amount > 0:               # validation: only positive deposits
            self.__balance += amount

    def show(self):
        print("Balance:", self.__balance)

acc = Account()
acc.deposit(100)
acc.deposit(-50)        # ignored — not a positive amount
acc.show()              # Balance: 100

# Trying to reach the private attribute from outside fails:
try:
    print(acc.__balance)
except AttributeError as e:
    print("Can't access it directly:", e)
