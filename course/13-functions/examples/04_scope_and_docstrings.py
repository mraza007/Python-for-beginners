"""Local scope, and documenting with a docstring.

Run me:  python 04_scope_and_docstrings.py
"""

def add(x, y):
    """Return the sum of x and y."""
    result = x + y      # 'result' exists only inside add()
    return result

print(add(2, 3))        # 5
print(add.__doc__)      # Return the sum of x and y.

# 'result' was local to add() — it doesn't exist out here:
# print(result)         # NameError
