"""Python figures out the type for you (dynamic typing).

Unlike Java or C++, you never declare "this is an int".
You can even point the same name at a different type later.

Run me:  python 02_dynamic_typing.py
"""

x = 100          # right now x is an integer
print(x, type(x))

x = "hello"      # now the SAME name points to a string
print(x, type(x))

# type() tells you what kind of value a name currently points to.
price = 9.99
print(type(price))   # <class 'float'>  -> a number with a decimal point
