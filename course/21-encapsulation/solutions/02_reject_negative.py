"""Solution — Exercise 2: Reject invalid deposits."""

class BankAccount:
    def __init__(self):
        self.__balance = 0

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount

    def get_balance(self):
        return self.__balance

acc = BankAccount()
acc.deposit(-20)   # ignored
acc.deposit(30)
print(acc.get_balance())
