"""Arithmetic operators and augmented assignment.

Run me:  python 02_arithmetic_operators.py
"""

print(10 + 3, 10 - 3, 10 * 3)   # 13 7 30
print(10 / 3)    # 3.3333333333333335  (always a float)
print(10 // 3)   # 3   floor division
print(10 % 3)    # 1   remainder
print(2 ** 4)    # 16  power

# Augmented assignment updates a variable using its own value.
total = 0
total += 5       # total = total + 5
total *= 2       # total = total * 2
print(total)     # 10
