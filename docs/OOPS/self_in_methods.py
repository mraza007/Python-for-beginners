'''
In the below code, how does return_product() method know which mobile object we are using?
'''

class Mobile:
    def __init__(self,price,brand):
        print ("Mobile created with id", id(self))
        self.price = price
        self.brand = brand

    def return_product(self):
        print ("Mobile being returned has id", id(self))
        print ("Brand being returned is ",self.brand," and price is ",self.price)

mob1=Mobile(1000,"Apple")

mob2=Mobile(2000,"Samsung")

mob2.return_product()
