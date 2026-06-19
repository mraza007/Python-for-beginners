"""Append to a file instead of overwriting it.

Run me:  python 03_append.py
"""

with open("log.txt", "w") as f:    # "w" starts fresh
    f.write("line 1\n")

with open("log.txt", "a") as f:    # "a" adds to the end
    f.write("line 2\n")

with open("log.txt") as f:
    print(f.read())

import os
os.remove("log.txt")
