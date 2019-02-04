'''
Just like the balloon with multiple ribbons, if we change the attribute of an object 
through one reference variable, it immediately reflects in other reference variable as 
there is only one balloon ultimately!
'''

class Mobile:
    def __init__(self, price, brand):
        self.price = price
        self.brand = brand

mob1=Mobile(1000, "Apple")
print("Price of mobile 1 :", mob1.price)

mob2=mob1
mob2.price=3000

print("Price of mobile 1 :", mob1.price)
print("Price of mobile 2 :", mob2.price)
