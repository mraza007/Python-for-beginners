"""Parameters (inputs) and return (output).

Run me:  python 02_parameters_and_return.py
"""

def square(num):
    return num * num

result = square(5)
print(result)      # 25
print(square(3))   # 9

def add(a, b):
    return a + b

print(add(2, 4))   # 6
# a, b are PARAMETERS; the 2 and 4 are ARGUMENTS. Order matters.

# A function with no return hands back None.
def shout(text):
    print(text.upper())

value = shout("hi")   # prints HI
print(value)          # None
