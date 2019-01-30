'''
For a readable output when printing an object we can use the inbuilt special __str__ method. 
This method MUST return a string and this string will be used when the object is printed. 
This is useful in debugging as we can print the values of the attributes
'''

class Shoe:
    def __init__(self, price, material):
        self.price = price
        self.material = material

    def __str__(self):
       return "Shoe with price: " + str(self.price) + " and material: " + self.material

s1=Shoe(1000, "Canvas")
print(s1)
