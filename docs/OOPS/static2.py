'''
However, the solution of hardcoding the value in the attribute is not a good one. 
For example, since this is a limited time discount we should be able to programmatically 
enable and disable the discount using functions like this:
'''


class Mobile:
    def __init__(self, price, brand):
        self.price = price
        self.brand = brand
        self.discount = 0

    def purchase(self):
        total = self.price - self.price * self.discount / 100
        print (self.brand, "mobile with price", self.price, "is available after discount at", total)

def enable_discount(list_of_mobiles):
    for mobile in list_of_mobiles:
        mobile.discount=50

def disable_discount(list_of_mobiles):
    for mobile in list_of_mobiles:
        mobile.discount=0

mob1=Mobile(20000, "Apple")
mob2=Mobile(30000, "Apple")
mob3=Mobile(5000, "Samsung")
mob4=Mobile(6000, "Samsung")

list_of_mobiles=[mob1,mob2,mob3,mob4]

mob1.purchase()

enable_discount(list_of_mobiles)

mob2.purchase()
mob3.purchase()

disable_discount(list_of_mobiles)

mob4.purchase()


'''
However, in our current approach, each object has discount as an attribute. 
If we change the value for one object, it does not affect the other object. 
If we have to change, we have to change for all the objects, one by one.
'''
