"""Read a traceback from the bottom up.

Run me:  python 02_reading_traceback.py
"""

import traceback

def step_three():
    return 1 / 0        # the actual bug lives here

def step_two():
    return step_three()

def step_one():
    return step_two()

try:
    step_one()
except ZeroDivisionError:
    # Normally Python prints this automatically when a program crashes.
    traceback.print_exc()

print()
print("Read it bottom-up: the LAST line is the error (ZeroDivisionError),")
print("and the lines above trace the calls that led there — step_three is the culprit.")
