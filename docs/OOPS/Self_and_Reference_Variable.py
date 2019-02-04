'''
mob2.return_product() can also be invoked as Mobile.return_product(mob2)

Thus self now refers to mob2, as this is actually pass by reference. 
For simplicity sake and for better readability we use mob2.return_product() instead of Mobile.return_product(mob2)
'''

class Mobile:
    def __init__(self,price,brand):
        print (id(self))
        self.price = price
        self.brand = brand

    def return_product(self):
        print (id(self))
        print ("Brand being returned is ",self.brand," and price is ",self.price)

mob1 = Mobile(1000, "Apple")
print ("Mobile 1 has id", id(mob1))

mob2=Mobile(2000, "Samsung")
print ("Mobile 2 has id", id(mob2))

mob2.return_product()
Mobile.return_product(mob2)
