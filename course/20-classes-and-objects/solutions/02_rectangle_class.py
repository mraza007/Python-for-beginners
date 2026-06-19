"""Solution — Exercise 2: A Rectangle class."""

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

r = Rectangle(8, 5)
print(r.area())
