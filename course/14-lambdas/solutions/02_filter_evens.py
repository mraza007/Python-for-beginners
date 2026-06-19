"""Solution — Exercise 2: Keep the even numbers (with filter)."""

numbers = [1, 2, 3, 4, 5, 6, 7, 8]

evens = filter(lambda x: x % 2 == 0, numbers)
print(list(evens))
