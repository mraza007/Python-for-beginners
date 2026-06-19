"""else runs on success; finally always runs.

Run me:  python 03_else_finally.py
"""

try:
    result = 10 / 2
except ZeroDivisionError:
    print("Division failed")
else:
    print("Success:", result)   # runs only if there was no exception
finally:
    print("This always runs")   # runs no matter what — great for cleanup
