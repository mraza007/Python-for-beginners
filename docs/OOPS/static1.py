#Need for static

'''
Let us assume that in our online shopping app, we want to provide a limited 50% flat off on all mobile phones.
How can we write our code so that all mobile objects get a 50% off? 
One solution is to create a discount attribute and hard code the value as 50% as shown below:
'''

class Mobile:
    def __init__(self, price, brand):
        self.price = price
        self.brand = brand
        self.discount = 50

    def purchase(self):
        total = self.price - self.price * self.discount / 100
        print (self.brand, "mobile with price", self.price, "is available after discount at", total)

mob1=Mobile(20000, "Apple")
mob2=Mobile(30000, "Apple")
mob3=Mobile(5000, "Samsung")

mob1.purchase()
mob2.purchase()
