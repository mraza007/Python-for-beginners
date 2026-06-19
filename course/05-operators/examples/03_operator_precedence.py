"""Operator precedence — the order Python applies operators.

Run me:  python 03_operator_precedence.py
"""

# Multiplication/division happen before addition/subtraction.
print(2 + 3 * 4)     # 14   (3 * 4 first, then + 2)
print((2 + 3) * 4)   # 20   (parentheses force + first)

# ** (power) happens before * and /.
print(2 * 3 ** 2)    # 18   (3 ** 2 = 9, then * 2)

# Same-level operators go left to right.
print(10 - 2 - 3)    # 5

# When in doubt, add parentheses to say exactly what you mean.
print((10 - 2) - 3)  # 5
