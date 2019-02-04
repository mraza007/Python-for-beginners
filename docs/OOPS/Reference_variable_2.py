'''
Just like a balloon without a ribbon, an object without a reference variable cannot be used later.
'''
class Mobile:
    def __init__(self, price, brand):
        self.price = price
        self.brand = brand

Mobile(1000, "Apple")
#After the above line the Mobile
# object created is lost and unusable
