"""Default values and keyword arguments.

Run me:  python 03_default_and_keyword_arguments.py
"""

def power(base, exponent=2):
    return base ** exponent

print(power(5))       # 25   exponent defaults to 2
print(power(5, 3))    # 125  passed positionally

# Keyword arguments: pass by name, in any order.
print(power(exponent=3, base=2))   # 8
