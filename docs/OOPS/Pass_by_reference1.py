'''
What happens when we pass an object as a parameter to a function? In the below code, what will be the output?
'''


class Mobile:
    def __init__(self, price, brand):
        self.price = price
        self.brand = brand

def change_price(mobile_obj):
    mobile_obj.price = 3000

mob1=Mobile(1000, "Apple")
change_price(mob1)
print (mob1.price)
