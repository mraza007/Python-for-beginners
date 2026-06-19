"""Exercise 1 — Fix the average.

The line below is meant to average three test scores, but precedence is wrong:
8 + 10 + 12 / 3 divides only 12 by 3, giving 22.0 instead of 10.0.

TODO:
  * Add parentheses so `average` correctly equals (8 + 10 + 12) / 3.
  * Print exactly:  Average: 10.0

Expected output:
  Average: 10.0

Run:  python 01_fix_precedence.py
Check yourself against ../solutions/01_fix_precedence.py
"""

# TODO: fix the parentheses on the next line
average = 8 + 10 + 12 / 3

print(f"Average: {average}")
