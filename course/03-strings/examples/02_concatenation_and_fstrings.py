"""Joining strings: +, +=, and f-strings.

Run me:  python 02_concatenation_and_fstrings.py
"""

first = "Hello"
second = "World"
print(first + " " + second)   # Hello World   (+ glues strings together)

greeting = "Hi"
greeting += "!"               # += appends to the end
print(greeting)               # Hi!

# The cleanest way to mix text and variables is an f-string.
name = "Ada"
age = 36
print(f"{name} is {age} years old.")   # Ada is 36 years old.

# You can't glue text to a number directly:
# print("age: " + age)   # TypeError
# ...but str() converts it, and f-strings do this for you automatically.
print("age: " + str(age))    # age: 36
