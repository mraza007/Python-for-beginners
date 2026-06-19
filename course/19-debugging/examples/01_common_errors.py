"""Trigger and read the most common errors (caught, so we can print them).

Run me:  python 01_common_errors.py
"""

try:
    print(undefined_variable)      # not defined anywhere
except NameError as e:
    print("NameError:", e)

try:
    print("age: " + 5)             # can't add str and int
except TypeError as e:
    print("TypeError:", e)

try:
    print([1, 2, 3][10])           # index out of range
except IndexError as e:
    print("IndexError:", e)

try:
    print({"a": 1}["b"])           # no such key
except KeyError as e:
    print("KeyError:", e)

try:
    print(int("abc"))              # right type (str), wrong value
except ValueError as e:
    print("ValueError:", e)
