"""Checking for keys, removing, and bulk-updating.

Run me:  python 03_methods.py
"""

inv = {"apples": 5, "pears": 2}

print("apples" in inv)   # True    (in checks the KEYS)
print("milk" in inv)     # False

removed = inv.pop("pears")   # remove a key and get its value back
print(removed)               # 2
print(inv)                   # {'apples': 5}

inv.update({"apples": 10, "bread": 3})   # update existing + add new
print(inv)                   # {'apples': 10, 'bread': 3}
