'''
An object is like a balloon and the reference variable is like the ribbon connecting it to the ground.
'''

class Mobile:
    def __init__(self, price, brand):
        self.price = price
        self.brand = brand

mob1=Mobile(1000, "Apple")
print(mob1.price)
#We are able to access the object
#in subsequent lines because we
#have a reference variable. This is
#like holding a balloon with a ribbon
