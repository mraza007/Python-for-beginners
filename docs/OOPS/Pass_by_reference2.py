'''
When we pass an object to a parameter, the parameter name becomes a reference variable.

Recollecting the balloon example, it is like creating one more ribbon to the same balloon. 
Thus there is one object with two reference variable, one the formal parameter and the actual parameter. 
Thus any change made through one reference variable will affect the other as well.
'''

class Mobile:
    def __init__(self, price, brand):
        self.price = price
        self.brand = brand

    def change_price(mobile_obj):
        print ("Id of object inside function", id(mobile_obj))
        mobile_obj.price=3000

mob1=Mobile(1000, "Apple")
print ("Id of object in driver code", id(mob1))

mob1.change_price()
print ("Price of mob1 ", mob1.price)
