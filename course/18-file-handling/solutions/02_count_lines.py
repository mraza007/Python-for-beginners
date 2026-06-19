"""Solution — Exercise 2: Write some lines, then count them."""

import os

with open("data.txt", "w") as f:
    f.write("one\ntwo\nthree\n")

with open("data.txt") as f:
    lines = f.readlines()

print(f"Lines: {len(lines)}")

os.remove("data.txt")
