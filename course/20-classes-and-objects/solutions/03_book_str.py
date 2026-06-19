"""Solution — Exercise 3: Make a Book print nicely."""

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return f"{self.title} by {self.author}"

print(Book("Python", "Guido"))
