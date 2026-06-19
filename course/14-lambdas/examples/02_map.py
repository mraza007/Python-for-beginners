"""map() applies a function to every item.

Run me:  python 02_map.py
"""

nums = [1, 2, 3, 4, 5]

squared = map(lambda x: x * x, nums)

# map returns an iterator, so wrap it in list() to see the values.
print(list(squared))   # [1, 4, 9, 16, 25]

# Another example: turn numbers into strings.
labels = map(lambda n: f"#{n}", nums)
print(list(labels))    # ['#1', '#2', '#3', '#4', '#5']
