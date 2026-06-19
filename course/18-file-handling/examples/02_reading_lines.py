"""Read a file one line at a time.

Run me:  python 02_reading_lines.py
"""

# First create a file to read from.
with open("fruits.txt", "w") as f:
    f.write("apple\nbanana\ncherry\n")

# Looping over a file yields one line at a time (with its newline).
with open("fruits.txt") as f:
    for line in f:
        print(line.strip())   # strip() removes the trailing newline

import os
os.remove("fruits.txt")
