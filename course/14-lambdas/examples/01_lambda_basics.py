"""A lambda is a tiny, unnamed function.

Run me:  python 01_lambda_basics.py
"""

def square(x):       # a normal function
    return x * x

square2 = lambda x: x * x   # the same idea, written as a lambda

print(square(4))     # 16
print(square2(4))    # 16

# Lambdas can take several arguments. They return the expression automatically.
add = lambda a, b: a + b
print(add(2, 3))     # 5
