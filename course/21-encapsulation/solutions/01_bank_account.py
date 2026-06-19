"""Solution — Exercise 1: A bank account with a private balance."""

class BankAccount:
    def __init__(self):
        self.__balance = 0

    def deposit(self, amount):
        self.__balance += amount

    def get_balance(self):
        return self.__balance

acc = BankAccount()
acc.deposit(100)
acc.deposit(50)
print(acc.get_balance())
