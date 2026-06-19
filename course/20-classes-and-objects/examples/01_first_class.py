"""Your first class, and creating objects from it.

Run me:  python 01_first_class.py
"""

class Dog:
    def __init__(self, name):     # constructor: runs when a Dog is created
        self.name = name          # store data on THIS object

    def bark(self):               # a method belonging to the class
        return f"{self.name} says Woof!"

rex = Dog("Rex")        # create (instantiate) objects
fido = Dog("Fido")

print(rex.name)         # Rex
print(rex.bark())       # Rex says Woof!
print(fido.bark())      # Fido says Woof!
