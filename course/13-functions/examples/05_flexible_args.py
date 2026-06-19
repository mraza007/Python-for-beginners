"""*args: accept any number of arguments.

Run me:  python 05_flexible_args.py
"""

def total(*numbers):
    # The * gathers every argument into a tuple called 'numbers'.
    running = 0
    for n in numbers:
        running += n
    return running

print(total(1, 2, 3))          # 6
print(total(10, 20, 30, 40))   # 100
print(total())                 # 0  (no arguments is fine)
