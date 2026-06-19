# 09 · Lists

> **Part 2 — Data Structures** · Estimated time: 30–40 min · Prerequisite: 07 · Loops

A **list** holds many values in a single, ordered container — a shopping list, a
set of scores, a row of names. Lists are the workhorse data structure of Python:
you can add to them, remove from them, sort them, and loop over them.

## What you'll learn
- Creating lists and reading items by **index** (and with `in`)
- Measuring length with `len()`
- Changing a list: `append`, `insert`, `extend`, `remove`, `pop`
- Slicing, and sorting with `sort()` vs `sorted()`
- Looping over a list to process every item

---

## 1. Creating and accessing

```python
fruits = ["apple", "banana", "cherry"]
print(len(fruits))         # 3
print(fruits[0])           # apple    (indexing starts at 0)
print(fruits[-1])          # cherry   (negative counts from the end)
print("banana" in fruits)  # True     (membership test)
```

A list can mix types (`[1, "two", 3.0]`), though most lists hold one kind of
thing.

▶️ **Run it:** `python examples/01_creating_and_accessing.py`

---

## 2. Changing a list

Lists are **mutable** — you can change them after creating them.

```python
nums = [1, 2, 3]
nums.append(4)        # add one item to the end   -> [1, 2, 3, 4]
nums.insert(0, 0)     # insert at a position       -> [0, 1, 2, 3, 4]
nums.extend([5, 6])   # add several items          -> [0, 1, 2, 3, 4, 5, 6]

nums.remove(0)        # remove the first matching value (0)
last = nums.pop()     # remove AND return the last item (6)
print(nums, "popped", last)
```

▶️ **Run it:** `python examples/02_modifying.py`

---

## 3. Slicing and sorting

Slicing works just like it did for strings: `list[start:stop]`.

```python
letters = ["d", "a", "c", "b"]
print(letters[1:3])      # ['a', 'c']

print(sorted(letters))   # ['a', 'b', 'c', 'd']  -> returns a NEW list
print(letters)           # unchanged

letters.sort()           # sorts THIS list in place (returns None)
print(letters)           # ['a', 'b', 'c', 'd']
```

> ⚠️ `sorted(x)` gives you a new sorted list; `x.sort()` rearranges `x` itself
> and returns `None`. Writing `x = x.sort()` is a classic bug — it sets `x` to
> `None`.

▶️ **Run it:** `python examples/03_slicing_and_sorting.py`

> 💡 **Try it yourself:** reverse a list two ways — with `.reverse()` and with
> the slice `x[::-1]`. Which one changes the original?

---

## 4. Looping over a list

```python
scores = [10, 20, 30]
for score in scores:
    print(score)

total = 0
for score in scores:
    total += score
print("Total:", total)   # 60
```

(Python also has `sum(scores)` and `max(scores)` built in — handy shortcuts.)

▶️ **Run it:** `python examples/04_looping.py`

---

## Common mistakes

| Mistake | What happens | Fix |
|---|---|---|
| `fruits[3]` on a 3-item list | `IndexError` | Valid indexes are `0`..`len-1`; last is `-1`. |
| `x = x.sort()` | `x` becomes `None` | Use `x.sort()` alone, or `x = sorted(x)`. |
| `nums.append([5, 6])` to add two items | nests a list inside | Use `extend([5, 6])` to add items individually. |
| `remove(x)` when `x` isn't there | `ValueError` | Check `if x in list:` first. |

---

## Recap / cheat-sheet

```python
items = [1, 2, 3]
len(items)            # 3
items[0]  items[-1]   # first / last
x in items            # membership -> True/False

items.append(4)       # add one to the end
items.insert(0, 9)    # add at a position
items.extend([5, 6])  # add several
items.remove(9)       # remove by value
items.pop()           # remove & return the last

items[1:3]            # slice
sorted(items)         # new sorted list
items.sort()          # sort in place (returns None)
items.reverse()       # reverse in place
```

---

## Exercises

Run a file with `python exercises/<file>.py`, then compare with the matching
file in [`solutions/`](solutions/).

1. [`exercises/01_third_item.py`](exercises/01_third_item.py) — read items by index.
2. [`exercises/02_shopping_list.py`](exercises/02_shopping_list.py) — add and remove items, then report the list.
3. [`exercises/03_total_and_max.py`](exercises/03_total_and_max.py) — total and largest value of a number list.

> Try each yourself **before** opening the solution.

---

Next → **10 · Tuples & Sets** _(coming soon)_
