"""Your first variables.

Run me:  python 01_first_variable.py
"""

# A variable is a name that points to a value.
# Use a single equals sign (=) to assign a value to a name.
name = "Ada"
age = 36

# Now we can use those names anywhere we'd use the value.
print(name)
print(age)

# f-strings (note the f before the quotes) let us drop variables
# straight into text using {curly braces}.
print(f"{name} is {age} years old.")
