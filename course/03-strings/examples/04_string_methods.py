"""Useful string methods — and a note on immutability.

A method is a function attached to a value; call it with a dot.

Run me:  python 04_string_methods.py
"""

text = "  Hello World  "

print(text.upper())              # "  HELLO WORLD  "
print(text.lower())              # "  hello world  "
print(text.strip())              # "Hello World"  (trims spaces at both ends)
print(text.replace("o", "0"))    # "  Hell0 W0rld  "

print("a,b,c".split(","))        # ['a', 'b', 'c']  -> a list
print("-".join(["a", "b", "c"])) # "a-b-c"

print("hello".startswith("he"))  # True

# Strings are IMMUTABLE: methods return a NEW string; the original is unchanged.
original = "hello"
shouted = original.upper()
print(original)   # hello   (still the same)
print(shouted)    # HELLO
# original[0] = "J"   # TypeError: strings can't be changed in place
