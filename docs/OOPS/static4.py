#Accessing Static Variables

'''
Now that we have created static variables, we can access them using the Class name itself. 
Static variable belong to the class and not an object. 
Hence we don’t need self to access static variables.
'''

class Mobile:
    discount = 50
    def __init__(self, price, brand):
        self.price = price
        self.brand = brand

    def purchase(self):
        total = self.price - self.price * Mobile.discount / 100
        print (self.brand, "mobile with price", self.price, "is available after discount at", total)

mob1=Mobile(20000, "Apple")
mob2=Mobile(30000, "Apple")
mob3=Mobile(5000, "Samsung")

mob1.purchase()
mob2.purchase()
mob3.purchase()
