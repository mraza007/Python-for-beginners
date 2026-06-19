"""filter() keeps items where the function returns True.

Run me:  python 03_filter.py
"""

nums = [1, 2, 3, 4, 5, 6, 7, 8]

evens = filter(lambda x: x % 2 == 0, nums)
print(list(evens))     # [2, 4, 6, 8]

words = ["hi", "hello", "hey", "yo"]
long_words = filter(lambda w: len(w) > 3, words)
print(list(long_words))  # ['hello']
