'''
We can also store a number of objects inside a list or a dictionary. 
The below example, we have a list of mobile objects and we are iterating over the list and printing the values
'''

class Mobile:
    def __init__(self, brand, price):
        self.brand = brand
        self.price = price

mob1=Mobile("Apple", 1000)
mob2=Mobile("Samsung", 2000)
mob3=Mobile("Apple", 3000)
mob4=Mobile("Samsung", 4000)
mob5=Mobile("Apple", 5000)

list_of_mobiles=[mob1, mob2, mob3, mob4, mob5]

for mobile in list_of_mobiles:
    print (mobile.brand,mobile.price)
    


'''
What do you think will be the output of the below code?
'''

class Mobile:
    def __init__(self,brand,price):
        self.brand = brand
        self.price = price

mob1=Mobile("Apple", 1000)
mob2=Mobile("Samsung", 2000)
mob3=Mobile("Apple", 3000)


list_of_mobiles=[mob1, mob2, mob3]

mob3.brand="Samsung"

for mobile in list_of_mobiles:
    print (mobile.brand, mobile.price)
