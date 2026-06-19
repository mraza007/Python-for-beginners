"""Catch an error with try/except so the program doesn't crash.

Run me:  python 01_try_except.py
"""

try:
    number = int("abc")        # this raises ValueError
    print(number)              # never reached
except ValueError:
    print("That wasn't a valid number.")

print("The program keeps running.")
