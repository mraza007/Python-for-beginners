"""print() with several values, plus sep= and end=.

Run me:  python 01_print_options.py
"""

print("a", "b", "c")            # a b c   (default: a space between values)
print("a", "b", "c", sep="-")   # a-b-c   (sep changes the separator)
print("a", "b", "c", sep="")    # abc     (no separator)

print("Loading", end="...")     # don't end the line yet
print("done")                   # Loading...done  (continues the same line)
