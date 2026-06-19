# 12 · Comprehensions

> **Part 2 — Data Structures** · Estimated time: 25–35 min · Prerequisite: 09 · Lists

A **comprehension** is a compact, readable way to build a list (or dict or set)
from another collection. Anywhere you'd write a loop that creates an empty list
and `append`s to it, a comprehension often does the same job in one clear line.
This is one of Python's most loved features.

## What you'll learn
- Turning a build-a-list loop into a **list comprehension**
- **Filtering** items with an `if` inside a comprehension
- **Dict** and **set** comprehensions

---

## 1. List comprehensions

Compare the two ways to build a list of squares:

```python
nums = [1, 2, 3, 4, 5]

# The long way:
squares = []
for n in nums:
    squares.append(n * n)

# The comprehension — same result, one line:
squares = [n * n for n in nums]
print(squares)   # [1, 4, 9, 16, 25]
```

Read it left to right: *"`n * n` for each `n` in `nums`."* The pattern is
`[expression for item in iterable]`.

▶️ **Run it:** `python examples/01_list_comprehension.py`

---

## 2. Filtering with `if`

Add an `if` at the end to keep only the items you want.

```python
nums = [1, 2, 3, 4, 5, 6, 7, 8]

evens = [n for n in nums if n % 2 == 0]
print(evens)        # [2, 4, 6, 8]

# Transform and filter at the same time:
big_squares = [n * n for n in nums if n > 5]
print(big_squares)  # [36, 49, 64]
```

The pattern is `[expression for item in iterable if condition]`.

▶️ **Run it:** `python examples/02_filtering.py`

> 💡 **Try it yourself:** from `["hi", "hello", "hey", "yo"]`, build a list of
> only the words longer than 2 letters.

---

## 3. Dict and set comprehensions

The same idea works with `{}` to build dictionaries and sets.

```python
words = ["apple", "banana", "cherry"]

# Dict comprehension: build key: value pairs.
lengths = {w: len(w) for w in words}
print(lengths)   # {'apple': 5, 'banana': 6, 'cherry': 6}

# Set comprehension: unique results.
nums = [1, 2, 2, 3, 3, 3]
squares = {n * n for n in nums}
print(sorted(squares))   # [1, 4, 9]
```

▶️ **Run it:** `python examples/03_dict_and_set_comprehensions.py`

---

## Common mistakes

| Mistake | What happens | Fix |
|---|---|---|
| Cramming complex logic in | unreadable one-liner | If it needs more than a simple `if`, use a normal loop. |
| Using `()` and expecting a tuple | you get a **generator**, not a tuple | Use `[]` for a list; `tuple(...)` if you really want a tuple. |
| Forgetting the `if` goes at the end | `SyntaxError` | Order is `[expr for x in xs if cond]`. |
| Putting `:` in a list comprehension | that's dict syntax | Use `key: value` only inside `{}`. |

---

## Recap / cheat-sheet

```python
[expr for x in xs]              # list comprehension
[expr for x in xs if cond]     # with a filter
{k: v for x in xs}             # dict comprehension
{expr for x in xs}             # set comprehension (unique results)

# Equivalent loop for the first line:
out = []
for x in xs:
    out.append(expr)
```

---

## Exercises

Run a file with `python exercises/<file>.py`, then compare with the matching
file in [`solutions/`](solutions/).

1. [`exercises/01_squares.py`](exercises/01_squares.py) — build a list of squares.
2. [`exercises/02_even_numbers.py`](exercises/02_even_numbers.py) — filter out the even numbers.
3. [`exercises/03_word_lengths.py`](exercises/03_word_lengths.py) — map each word to its length with a dict comprehension.

> Try each yourself **before** opening the solution.

---

Next → **13 · Functions** _(coming soon)_
