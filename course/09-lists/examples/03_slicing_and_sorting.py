"""Slicing, and the sort() vs sorted() difference.

Run me:  python 03_slicing_and_sorting.py
"""

letters = ["d", "a", "c", "b"]

print(letters[1:3])      # ['a', 'c']   slice [start:stop]

# sorted() returns a NEW list and leaves the original alone.
print(sorted(letters))   # ['a', 'b', 'c', 'd']
print(letters)           # ['d', 'a', 'c', 'b']  (unchanged)

# .sort() rearranges THIS list in place and returns None.
letters.sort()
print(letters)           # ['a', 'b', 'c', 'd']

letters.reverse()
print(letters)           # ['d', 'c', 'b', 'a']
