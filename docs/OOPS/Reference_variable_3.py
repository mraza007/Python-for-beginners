'''
Just like a balloon can have multiple ribbons, an object can also have multiple reference variables. 
Both the references are referring to the same object. 
When you assign an already created object to a variable, a new object is not created.
'''

class Mobile:
    def __init__(self, price, brand):
        print ("Inside constructor")
        self.price = price
        self.brand = brand

mob1=Mobile(1000, "Apple")
mob2=mob1
print ("Id of object referred by mob1 reference variable is :", id(mob1))
print ("Id of object referred by mob2 reference variable is :", id(mob2))
#mob1 and mob2 are reference variables to the same object
