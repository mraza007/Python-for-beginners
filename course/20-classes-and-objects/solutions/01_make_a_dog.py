"""Solution — Exercise 1: Make a Dog class."""

class Dog:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return f"{self.name} says Woof!"

rex = Dog("Rex")
print(rex.speak())
