"""Lists are mutable: add and remove items.

Run me:  python 02_modifying.py
"""

nums = [1, 2, 3]

nums.append(4)        # add one item to the end   -> [1, 2, 3, 4]
nums.insert(0, 0)     # insert at index 0         -> [0, 1, 2, 3, 4]
nums.extend([5, 6])   # add several items         -> [0, 1, 2, 3, 4, 5, 6]
print(nums)

nums.remove(0)        # remove the first matching value (0)
last = nums.pop()     # remove AND return the last item (6)
print(nums)           # [1, 2, 3, 4, 5]
print("popped:", last)  # popped: 6
