#Shared variables

'''
What we need is a way to make an attribute shared across objects. 
The data is shared by all objects, not owned by each object. 
Thus, by making a single change, it should reflect in all objects at one go. 
'''

#Static

'''
We can create shared attributes by placing them directly inside the class and not inside the constructor. 
And since this attribute is not owned by any one object, we don’t need the self to create this attribute. 
Such variables which are created at a class level are called static variables. 
Here discount is a static value.
'''


class Mobile:
    discount = 50
    def __init__(self, price, brand):
        self.price = price
        self.brand = brand
