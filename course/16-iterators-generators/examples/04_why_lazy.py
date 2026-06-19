"""Generators are lazy: values are produced only when asked for.

Run me:  python 04_why_lazy.py
"""

def naturals():
    n = 1
    while True:        # an infinite LIST would crash; an infinite generator is fine
        yield n
        n += 1

gen = naturals()
for value in gen:
    if value > 5:
        break          # we decide when to stop
    print(value)       # 1, 2, 3, 4, 5
