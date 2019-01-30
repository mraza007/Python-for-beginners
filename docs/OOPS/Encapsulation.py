'''
We can put a lock on that data by adding a double underscore in front of it.

Adding a double underscore makes the attribute a private attribute. 
Private attributes are those which are accessible only inside the class. 
This method of restricting access to our data is called encapsulation.
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
print(c1.__wallet_balance)
