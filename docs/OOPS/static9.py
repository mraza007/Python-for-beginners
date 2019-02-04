'''
We can access static methods directly using the class name, even without creating objects.
'''

class Mobile:
    __discount = 50
    def __init__(self, price, brand):
        self.price = price
        self.brand = brand

    def purchase(self):
        total = self.price - self.price * Mobile.__discount / 100
        print ("Total is ",total)

    @staticmethod
    def get_discount():
        return Mobile.__discount

    @staticmethod
    def set_discount(discount):
        Mobile.__discount = discount

print (Mobile.get_discount())
