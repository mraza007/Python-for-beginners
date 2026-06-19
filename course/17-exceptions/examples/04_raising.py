"""Raise your own exceptions to signal a problem.

Run me:  python 04_raising.py
"""

def set_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative")
    return age

print(set_age(30))      # 30  (fine)

# Catch the error we raised when the input is bad.
try:
    set_age(-1)
except ValueError as e:
    print("Caught:", e)
