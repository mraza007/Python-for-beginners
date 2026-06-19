"""Assign several names at once, and swap two values.

Run me:  python 04_multiple_assignment_and_swapping.py
"""

# Assign three names on one line.
x, y, z = 10, 11, 12
print(x, y, z)

# Give several names the SAME value.
a = b = c = 0
print(a, b, c)

# Swap two variables in a single line (a Python superpower).
# No temporary "third cup" needed.
left, right = "L", "R"
left, right = right, left
print(left, right)   # R L
