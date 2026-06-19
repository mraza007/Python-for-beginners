"""Combining conditions, and the one-line conditional expression.

Run me:  python 04_combining_conditions.py
"""

age = 25
has_ticket = True

# Both must be True for this block to run.
if age >= 18 and has_ticket:
    print("Enjoy the show!")

# Nesting: an if inside an if.
if has_ticket:
    if age < 18:
        print("Child ticket.")
    else:
        print("Adult ticket.")

# One-line conditional expression: value_if_true if condition else value_if_false
weather = "rain"
plan = "stay in" if weather == "rain" else "go out"
print(plan)   # stay in
