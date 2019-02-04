'''
We can also store objects in a dictionary. 
For example, in the below code we are storing all the mobile objects in a dictionary 
and printing only those mobiles whose price is greater than 3000
'''

class Mobile:
    def __init__(self,brand,price):
        self.brand = brand
        self.price = price

mob1=Mobile("Apple", 1000)
mob2=Mobile("Samsung", 5000)
mob3=Mobile("Apple", 3000)

mob_dict={
          "m1":mob1,
          "m2":mob2,
          "m3":mob3
          }

for key,value in mob_dict.items():
    if value.price > 3000:
        print (value.brand,value.price)
