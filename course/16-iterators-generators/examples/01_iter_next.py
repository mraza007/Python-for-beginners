"""Iterables, iterators, iter() and next().

Run me:  python 01_iter_next.py
"""

colors = ["red", "green", "blue"]
it = iter(colors)        # turn the iterable into an iterator

print(next(it))   # red
print(next(it))   # green
print(next(it))   # blue
# next(it)        # would raise StopIteration — nothing left

# A for loop does all of the above automatically.
for color in colors:
    print(color)
