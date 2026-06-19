"""From a build-a-list loop to a list comprehension.

Run me:  python 01_list_comprehension.py
"""

nums = [1, 2, 3, 4, 5]

# The long way: start empty and append.
squares = []
for n in nums:
    squares.append(n * n)
print(squares)   # [1, 4, 9, 16, 25]

# The comprehension: same result, one readable line.
squares = [n * n for n in nums]
print(squares)   # [1, 4, 9, 16, 25]

# It works on any iterable, like a range:
print([n * 2 for n in range(5)])   # [0, 2, 4, 6, 8]
