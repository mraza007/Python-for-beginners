"""The core data types, and how to inspect them.

Run me:  python 01_core_types.py
"""

age = 36           # int   — a whole number
price = 9.99       # float — a number with a decimal point
name = "Ada"       # str   — text
is_member = True   # bool  — True or False
nothing = None     # NoneType — "no value here yet"

# type() reports the category of a value.
print(age, type(age))
print(price, type(price))
print(name, type(name))
print(is_member, type(is_member))
print(nothing, type(nothing))
