"""Importing from the standard library.

Run me:  python 01_import_stdlib.py
"""

import math

print(math.sqrt(16))    # 4.0
print(math.pi)          # 3.141592653589793
print(math.floor(3.7))  # 3
print(math.ceil(3.2))   # 4

import random
random.seed(0)          # seeding makes the "random" result repeatable
print(random.randint(1, 6))   # a dice roll between 1 and 6
