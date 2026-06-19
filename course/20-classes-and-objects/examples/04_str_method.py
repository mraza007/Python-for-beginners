"""__str__ controls how an object looks when printed.

Run me:  python 04_str_method.py
"""

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return f"{self.title} by {self.author}"

b = Book("Python 101", "Guido")
print(b)          # Python 101 by Guido

# Without __str__, print(b) would show something like:
#   <__main__.Book object at 0x10a3f...>
