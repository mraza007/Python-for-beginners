'''
When we put a double underscore in front of the attribute name, python will internally change its name to _Classname__attribute.

Since we know that the name of the variable changes when we make it private, we can access it using its modified name as shown below:
'''
class Customer:
    def __init__(self, cust_id, name, age, wallet_balance):
        self.cust_id = cust_id
        self.name = name
        self.age = age
        self.__wallet_balance = wallet_balance

    def update_balance(self, amount):
        if amount < 1000 and amount > 0:
            self.__wallet_balance += amount

    def show_balance(self):
        print ("The balance is ",self.__wallet_balance)

c1=Customer(100, "Gopal", 24, 1000)
c1._Customer__wallet_balance = 10000000000
c1.show_balance()
