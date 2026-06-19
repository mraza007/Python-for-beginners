"""Expressions produce values; statements perform actions.

Run me:  python 01_expressions_vs_statements.py
"""

# Expressions evaluate to a value. We print them here to see that value.
print(3 + 4)            # 7
print("Hi " + "there")  # Hi there
print(18 >= 18)         # True

# Statements DO something. These two lines are statements:
x = 3 + 4               # an assignment statement (holds the expression 3 + 4)
print(x)                # a print statement (performs an action)

# Rule of thumb: if it could sit on the right of an =, it's an expression.
