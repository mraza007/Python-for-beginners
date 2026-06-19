"""The + and * operators also work on strings.

Run me:  python 04_string_operators.py
"""

print("ab" + "cd")   # abcd     + joins strings
print("ha" * 3)      # hahaha   * repeats a string
print("-" * 10)      # ----------  handy for separator lines

# Precedence applies here too: * runs before +, so "! " * 2 happens first.
name = "Sam"
print("Hi " + name + "! " * 2)   # Hi Sam! !
