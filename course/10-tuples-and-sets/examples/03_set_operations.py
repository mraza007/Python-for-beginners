"""Set maths: union, intersection, difference.

Run me:  python 03_set_operations.py
"""

a = {1, 2, 3, 4}
b = {3, 4, 5}

print(sorted(a | b))   # [1, 2, 3, 4, 5]  union: in either set
print(sorted(a & b))   # [3, 4]           intersection: in both sets
print(sorted(a - b))   # [1, 2]           difference: in a but not b
print(sorted(b - a))   # [5]              in b but not a
