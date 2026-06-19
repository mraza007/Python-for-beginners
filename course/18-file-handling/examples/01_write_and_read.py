"""Write a file, then read it back.

Run me:  python 01_write_and_read.py
"""

# "w" creates (or overwrites) the file. 'with' closes it automatically.
with open("sample.txt", "w") as f:
    f.write("Hello, file!\n")
    f.write("Second line.\n")

# "r" (the default) reads the file.
with open("sample.txt", "r") as f:
    contents = f.read()

print(contents)

import os
os.remove("sample.txt")   # tidy up so we don't leave files behind
