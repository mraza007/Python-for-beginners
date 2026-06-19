"""Converting between types — and the input() trap.

Run me:  python 03_type_conversion.py
"""

# Each core type has a function that converts TO it.
print(int("42"))      # 42    text -> whole number
print(float("3.14"))  # 3.14  text -> decimal
print(str(100))       # 100   number -> text (print shows no quotes)

# int() chops the decimal off; it does NOT round.
print(int(3.9))       # 3
print(round(3.9))     # 4   <- use round() when you actually want rounding

# Why this matters: text and numbers don't mix until you convert.
text = "5"
number = int(text)
print(number + 1)     # 6

# This would be an error (uncomment to see it):
# print("5" + 1)      # TypeError: can only concatenate str (not "int") to str
