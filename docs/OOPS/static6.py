#Static Variables and Encapsulation

'''
We can make our static variable as a private variable by adding a double underscore in front of it. 
We can also create getter and setter methods to access or modify it.
'''

class Mobile:
    __discount = 50

    def get_discount(self):
        return Mobile.__discount

    def set_discount(self,discount):
        Mobile.__discount = discount

m1=Mobile()
print(m1.get_discount())
