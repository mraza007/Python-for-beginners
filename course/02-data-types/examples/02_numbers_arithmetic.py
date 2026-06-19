"""Arithmetic with numbers, including //, % and **.

Run me:  python 02_numbers_arithmetic.py
"""

print(7 + 3)    # 10  addition
print(7 - 3)    # 4   subtraction
print(7 * 3)    # 21  multiplication

print(7 / 3)    # 2.3333333333333335  TRUE division -> always a float
print(7 // 3)   # 2   FLOOR division -> drops the remainder
print(7 % 3)    # 1   MODULO -> the remainder ("what's left over")
print(2 ** 3)   # 8   EXPONENT -> 2 to the power of 3

# Modulo is great for "is it even?" checks:
print(10 % 2)   # 0  -> 10 is even
print(7 % 2)    # 1  -> 7 is odd
