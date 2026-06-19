"""Catch specific exception types.

Run me:  python 02_specific_exceptions.py
"""

def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "You can't divide by zero!"

print(divide(10, 2))   # 5.0
print(divide(10, 0))   # You can't divide by zero!

# Catch more than one type at once, and grab the error with 'as'.
try:
    value = int("oops")
except (ValueError, TypeError) as e:
    print("Problem:", e)
