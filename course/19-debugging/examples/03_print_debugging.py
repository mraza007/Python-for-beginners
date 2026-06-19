"""Print-debugging: watch what your code actually does.

Run me:  python 03_print_debugging.py
"""

def double_all(numbers):
    result = []
    for n in numbers:
        print(f"DEBUG: processing {n}")   # temporary — remove once it works
        result.append(n * 2)
    return result

print(double_all([1, 2, 3]))
