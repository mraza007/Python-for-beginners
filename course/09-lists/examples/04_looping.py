"""Looping over a list to process every item.

Run me:  python 04_looping.py
"""

scores = [10, 20, 30]

# Visit each item in turn.
for score in scores:
    print(score)

# The accumulator pattern: build a running total.
total = 0
for score in scores:
    total += score
print("Total:", total)        # 60

# Python also has handy built-ins:
print("Sum:", sum(scores))    # 60
print("Max:", max(scores))    # 30
