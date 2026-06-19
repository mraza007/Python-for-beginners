# 10 · Tuples & Sets

> **Part 2 — Data Structures** · Estimated time: 25–35 min · Prerequisite: 09 · Lists

Lists aren't the only way to group values. A **tuple** is like a list that can't
be changed — perfect for fixed groups of data. A **set** is an unordered
collection that automatically removes duplicates — perfect for "unique things"
and for comparing groups.

## What you'll learn
- Creating tuples and why they're **immutable**
- **Unpacking** a tuple into separate variables
- Creating sets, and how they drop duplicates
- Set membership and the fact that sets have **no order / no index**
- Set maths: union `|`, intersection `&`, difference `-`

---

## 1. Tuples

A tuple uses parentheses and, once created, **cannot be changed**.

```python
point = (3, 4)
print(point[0])      # 3       (index like a list)
print(len(point))    # 2
# point[0] = 9       # TypeError — tuples are immutable

# Unpacking: hand each item to its own variable.
x, y = point
print(x, y)          # 3 4
```

Use a tuple for things that belong together and shouldn't change — coordinates,
a date as `(year, month, day)`, an RGB colour.

> Note: a one-item tuple needs a trailing comma — `(5,)`, not `(5)`.

▶️ **Run it:** `python examples/01_tuples.py`

---

## 2. Sets

A set uses curly braces and keeps only **unique** values.

```python
nums = {1, 2, 3, 2, 1}
print(nums)          # {1, 2, 3}  — duplicates gone (order may vary)
print(len(nums))     # 3

nums.add(4)          # add a value
nums.add(2)          # already present — no effect
nums.discard(1)      # remove a value (no error if it's missing)
print(2 in nums)     # True
```

Sets have **no order**, so there's no `nums[0]` — you can't index a set.

▶️ **Run it:** `python examples/02_sets.py`

---

## 3. Set maths

Sets shine when comparing groups.

```python
a = {1, 2, 3, 4}
b = {3, 4, 5}
print(sorted(a | b))   # [1, 2, 3, 4, 5]  union: in either
print(sorted(a & b))   # [3, 4]           intersection: in both
print(sorted(a - b))   # [1, 2]           difference: in a but not b
```

(We wrap results in `sorted()` only to print them in a predictable order.)

▶️ **Run it:** `python examples/03_set_operations.py`

> 💡 **Try it yourself:** given a list with repeats, how would you count how many
> *distinct* values it has? (Hint: turn it into a set.)

---

## Common mistakes

| Mistake | What happens | Fix |
|---|---|---|
| `point[0] = 9` on a tuple | `TypeError` | Tuples can't change; build a new tuple instead. |
| `(5)` expecting a tuple | that's just the number `5` in parentheses | A single-item tuple needs a comma: `(5,)`. |
| `my_set[0]` | `TypeError` — sets aren't indexable | Sets are unordered; loop over them or convert to a list. |
| Relying on set print order | order isn't guaranteed | Use `sorted(my_set)` when order matters. |

---

## Recap / cheat-sheet

```python
# Tuple — ordered, immutable
t = (3, 4)
t[0]                 # 3
x, y = t             # unpack

# Set — unordered, unique
s = {1, 2, 2, 3}     # -> {1, 2, 3}
s.add(4)             # add
s.discard(1)         # remove (safe if missing)
v in s               # membership
a | b   a & b   a - b   # union / intersection / difference
```

---

## Exercises

Run a file with `python exercises/<file>.py`, then compare with the matching
file in [`solutions/`](solutions/).

1. [`exercises/01_unpack_point.py`](exercises/01_unpack_point.py) — unpack a coordinate tuple.
2. [`exercises/02_unique_words.py`](exercises/02_unique_words.py) — count the distinct words with a set.
3. [`exercises/03_common_friends.py`](exercises/03_common_friends.py) — find friends two people share.

> Try each yourself **before** opening the solution.

---

Next → **11 · Dictionaries** _(coming soon)_
