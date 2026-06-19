"""sorted() with a custom key.

Run me:  python 04_sorted_key.py
"""

words = ["banana", "kiwi", "apple"]

print(sorted(words))                        # ['apple', 'banana', 'kiwi']  alphabetical
print(sorted(words, key=lambda w: len(w)))  # ['kiwi', 'apple', 'banana']  by length

print(sorted([3, 1, 2]))                    # [1, 2, 3]
print(sorted([3, 1, 2], reverse=True))      # [3, 2, 1]  descending
