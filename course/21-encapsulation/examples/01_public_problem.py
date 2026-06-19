"""Public data can be set to anything — even invalid values.

Run me:  python 01_public_problem.py
"""

class Account:
    def __init__(self):
        self.balance = 0      # fully public

acc = Account()
acc.balance = -9999           # nothing stops this nonsense
print(acc.balance)            # -9999  (an invalid balance!)
