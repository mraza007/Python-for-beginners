#Static Method continued

'''
Since static variable is object independent, we need a way to access the getter setter methods without an object. This is possible by creating static methods. Static methods are those methods which can be accessed without an object. They are accessed using the class name.

There are two rules in creating such static methods:

The methods should not have self
@staticmethod must be written on top of it

'''


@staticmethod
def get_discount():
    return Mobile.__discount
@staticmethod
def set_discount(discount):
    Mobile.__discount=discount
