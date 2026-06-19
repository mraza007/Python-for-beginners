"""Each object has its own independent data.

Run me:  python 03_multiple_objects.py
"""

class Counter:
    def __init__(self):
        self.value = 0

    def increment(self):
        self.value += 1

a = Counter()
b = Counter()

a.increment()
a.increment()
b.increment()

print("a:", a.value)   # 2
print("b:", b.value)   # 1   (b is completely independent of a)
