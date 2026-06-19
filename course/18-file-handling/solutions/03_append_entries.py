"""Solution — Exercise 3: Write, then append."""

import os

with open("diary.txt", "w") as f:
    f.write("Day 1\n")

with open("diary.txt", "a") as f:
    f.write("Day 2\n")

with open("diary.txt") as f:
    print(f.read().strip())

os.remove("diary.txt")
