"""Sets: unordered collections of unique values.

Run me:  python 02_sets.py
"""

nums = {1, 2, 3, 2, 1}
print(nums)          # {1, 2, 3}  — duplicates removed (order may vary)
print(len(nums))     # 3

nums.add(4)          # add a value
nums.add(2)          # already present — no change
nums.discard(1)      # remove a value (no error if missing)

print(2 in nums)     # True
print(sorted(nums))  # [2, 3, 4]  (sorted just for a tidy printout)

# Sets have no order, so there is no nums[0] — indexing a set is an error.
