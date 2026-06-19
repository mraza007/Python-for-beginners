"""Filtering items with an if inside a comprehension.

Run me:  python 02_filtering.py
"""

nums = [1, 2, 3, 4, 5, 6, 7, 8]

# Keep only the items where the condition is True.
evens = [n for n in nums if n % 2 == 0]
print(evens)         # [2, 4, 6, 8]

# Transform AND filter at the same time.
big_squares = [n * n for n in nums if n > 5]
print(big_squares)   # [36, 49, 64]

words = ["hi", "hello", "hey", "yo"]
short = [w for w in words if len(w) <= 2]
print(short)         # ['hi', 'yo']
