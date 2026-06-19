"""Truthiness: which everyday values act like True or False.

Run me:  python 04_truthiness.py
"""

# Falsy values (act like False):
print(bool(0))      # False
print(bool(0.0))    # False
print(bool(""))     # False   empty string
print(bool([]))     # False   empty list
print(bool(None))   # False

# Everything else is truthy (acts like True):
print(bool(42))     # True
print(bool("hi"))   # True
print(bool([1, 2])) # True
