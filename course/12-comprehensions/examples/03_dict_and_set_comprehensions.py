"""Dict and set comprehensions.

Run me:  python 03_dict_and_set_comprehensions.py
"""

words = ["apple", "banana", "cherry"]

# Dict comprehension: build key: value pairs.
lengths = {w: len(w) for w in words}
print(lengths)   # {'apple': 5, 'banana': 6, 'cherry': 6}

# Set comprehension: results are unique.
nums = [1, 2, 2, 3, 3, 3]
squares = {n * n for n in nums}
print(sorted(squares))   # [1, 4, 9]  (sorted just for a tidy printout)
