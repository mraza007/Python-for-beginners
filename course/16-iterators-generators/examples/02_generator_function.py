"""Generator functions use yield to produce values one at a time.

Run me:  python 02_generator_function.py
"""

def count_up(limit):
    n = 1
    while n <= limit:
        yield n        # hand back n, then PAUSE here until the next value is asked for
        n += 1

# Collect everything into a list to see all the values.
print(list(count_up(5)))   # [1, 2, 3, 4, 5]

# Or loop over the generator directly.
for value in count_up(3):
    print(value)           # 1, 2, 3
