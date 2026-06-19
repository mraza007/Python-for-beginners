"""Solution — Exercise 1: Save a note and read it back."""

import os

message = "Remember to practice!"

with open("note.txt", "w") as f:
    f.write(message)

with open("note.txt") as f:
    print(f.read())

os.remove("note.txt")
