"""Solution — Exercise 3: Sort words by length."""

words = ["banana", "kiwi", "apple"]

by_length = sorted(words, key=lambda w: len(w))
print(by_length)
