'''

<P1>

self is not a keyword. self refers to the current object being executed.
'''

class Mobile:
    def __init__(self, price, brand):
        print("Id of self in constructor", id(self))
        self.price = price
        self.brand = brand

mob1=Mobile(1000, "Apple")
print("Id of mob1 in driver code", id(mob1))

mob2=Mobile(1000, "Apple")
print("Id of mob2 in driver code", id(mob2))



'''

<P2>

We have already seen that reference_variable.attribute_name creates an attribute for that object. 
By using self.attribute_name and assigning a value we are creating attributes to the current object. 
The best practice is to create attributes inside the constructor.
'''

class Mobile:
    def __init__(self, price, brand):
        print("Id of self in constructor", id(self))
        self.price = price
        self.brand = brand

mob1=Mobile(1000, "Apple")
print("Id of mob1 in driver code", id(mob1))

mob2=Mobile(1000, "Apple")
print("Id of mob2 in driver code", id(mob2))



'''

<P3>

Attributes can be created only by using the self variable and the dot operator. 
Without self we are only creating a local variable and not an attribute.
'''

class Mobile:
    def __init__(self):
        print ("Inside the Mobile constructor")
        self.brand = None
        brand = "Apple" #This is a local variable.
        #Variables without self are local and they dont
        #affect the attributes.

        #Local varaibles cannot be accessed outside the init
        #Using self creates attributes which are
        #accessible in other methods as well

mob1=Mobile()
print(mob1.brand)#This does not print Apple
#This prints None because brand=Apple creates
#a local variable and it does not affect the attribute
