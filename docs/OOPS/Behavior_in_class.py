'''
We can access an attribute in a method by using self. 
Value of the attribute accessed inside the method is determined by the object used to invoke the method. 
For example, in the code below when we invoke purchase using mob1, attribute values (Apple and 20000) of mob1 are accessed. 
Similarly, when mob2 is used to invoke purchase, attribute values (Samsung and 3000) of mob2 are accessed in purchase().
'''

class Mobile:
    def __init__(self, brand, price):
        print("Inside constructor")
        self.brand = brand
        self.price = price

    def purchase(self):
        print("Purchasing a mobile")
        print("This mobile has brand", self.brand, "and price", self.price)

print("Mobile-1")
mob1=Mobile("Apple", 20000)
mob1.purchase()

print("Mobile-2")
mob2=Mobile("Samsung",3000)
mob2.purchase()
