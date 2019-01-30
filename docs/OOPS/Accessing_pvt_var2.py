'''
To have a error free way of accessing and updating private variables, we create specific methods for this. 
Those methods which are meant to set a value to a private variable are called setter methods and methods 
meant to access private variable values are called getter methods. 

The below code is an example of getter and setter methods:
'''

class Customer:
    def __init__(self, id, name, age, wallet_balance):
        self.id = id
        self.name = name
        self.age = age
        self.__wallet_balance = wallet_balance

    def set_wallet_balance(self, amount):
        if amount < 1000 and amount>  0:
            self.__wallet_balance = amount

    def get_wallet_balance(self):
        return self.__wallet_balance

c1=Customer(100, "Gopal", 24, 1000)
c1.set_wallet_balance(120)
print(c1.get_wallet_balance())
