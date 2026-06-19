"""Variables can change over time.

Run me:  python 03_reassigning_and_updating.py
"""

score = 0
print(f"Start:      {score}")

score = 10            # reassign to a brand-new value
print(f"After bonus: {score}")

score = score + 5     # use the OLD value to build the NEW value
print(f"After + 5:   {score}")

score += 5            # shorthand for: score = score + 5
print(f"After += 5:  {score}")

# The same shorthand works for the other operators too.
score -= 2
score *= 2
print(f"Final:       {score}")
