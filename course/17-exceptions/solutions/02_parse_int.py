"""Solution — Exercise 2: Parse an integer safely."""

value = "abc"

try:
    number = int(value)
    print(number)
except ValueError:
    print(f"'{value}' is not a whole number")
