"""Tuples: ordered and immutable.

Run me:  python 01_tuples.py
"""

point = (3, 4)
print(point)         # (3, 4)
print(point[0])      # 3   index like a list
print(len(point))    # 2

# Tuples can't be changed:
# point[0] = 9       # TypeError

# Unpacking: give each item its own variable name.
x, y = point
print(x, y)          # 3 4

# A one-item tuple needs a trailing comma:
single = (5,)
print(type(single))  # <class 'tuple'>

# Two useful tuple methods:
colors = ("red", "green", "red")
print(colors.count("red"))    # 2
print(colors.index("green"))  # 1
