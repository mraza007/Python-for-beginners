"""Combining booleans with and / or / not.

Run me:  python 03_logical_operators.py
"""

print(True and False)   # False  -> "and" needs BOTH to be True
print(True and True)    # True
print(True or False)    # True   -> "or" needs only ONE to be True
print(False or False)   # False
print(not True)         # False  -> "not" flips it
print(not False)        # True

# A realistic combination:
age = 25
print(age >= 18 and age < 65)   # True  -> an adult under 65
