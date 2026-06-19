"""Handle a file that doesn't exist.

Run me:  python 04_missing_file.py
"""

try:
    with open("missing.txt") as f:
        print(f.read())
except FileNotFoundError:
    print("That file doesn't exist yet.")
