"""Solution — Exercise 2: A countdown generator."""

def countdown(n):
    while n >= 1:
        yield n
        n -= 1

print(list(countdown(3)))
