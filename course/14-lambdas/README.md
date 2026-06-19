# 14 · Lambdas & map/filter

> **Part 3 — Functions & Modules** · Estimated time: 25–35 min · Prerequisite: 13 · Functions

A **lambda** is a tiny, one-line function with no name. You reach for one when
you need a quick function to hand to another function — most often `map`,
`filter`, or `sorted`. These tools let you transform and filter whole
collections with very little code.

## What you'll learn
- Writing a `lambda` and how it relates to a normal `def` function
- `map()` — apply a function to every item
- `filter()` — keep only the items that pass a test
- `sorted(..., key=...)` — sort by a custom rule

---

## 1. Lambda basics

```python
def square(x):       # a normal function
    return x * x

square2 = lambda x: x * x   # the same idea, as a lambda

print(square(4))     # 16
print(square2(4))    # 16

add = lambda a, b: a + b    # lambdas can take several arguments
print(add(2, 3))     # 5
```

A lambda is just `lambda arguments: expression`. It automatically returns the
expression — no `return` keyword. If a function needs more than one line, use a
normal `def` instead.

▶️ **Run it:** `python examples/01_lambda_basics.py`

---

## 2. `map()` — transform every item

```python
nums = [1, 2, 3, 4, 5]

squared = map(lambda x: x * x, nums)   # apply the lambda to each item

# map returns an iterator — wrap it in list() to see the values.
print(list(squared))   # [1, 4, 9, 16, 25]
```

▶️ **Run it:** `python examples/02_map.py`

---

## 3. `filter()` — keep some items

`filter` keeps only the items for which the function returns `True`.

```python
nums = [1, 2, 3, 4, 5, 6, 7, 8]

evens = filter(lambda x: x % 2 == 0, nums)
print(list(evens))     # [2, 4, 6, 8]
```

▶️ **Run it:** `python examples/03_filter.py`

> 💡 **Try it yourself:** use `filter` to keep only the words longer than 3
> letters from `["hi", "hello", "hey", "yo"]`.

---

## 4. `sorted(key=...)` — sort your way

Pass `key=` a function that returns the value to sort *by*.

```python
words = ["banana", "kiwi", "apple"]

print(sorted(words))                       # ['apple', 'banana', 'kiwi'] (alphabetical)
print(sorted(words, key=lambda w: len(w))) # ['kiwi', 'apple', 'banana'] (by length)
print(sorted([3, 1, 2], reverse=True))     # [3, 2, 1] (descending)
```

▶️ **Run it:** `python examples/04_sorted_key.py`

---

## Common mistakes

| Mistake | What happens | Fix |
|---|---|---|
| `print(map(...))` | prints `<map object ...>` | Wrap it: `print(list(map(...)))`. |
| Putting a statement in a lambda | `SyntaxError` | Lambdas hold one *expression*; use `def` for logic. |
| Re-using a `map`/`filter` result twice | it's empty the second time (iterators exhaust) | Save it as a list: `result = list(map(...))`. |
| `sorted(x, key=len())` | calls `len` with no args — error | Pass the function itself: `key=len` or `key=lambda w: len(w)`. |

---

## Recap / cheat-sheet

```python
f = lambda x: x * 2          # one-line function
lambda a, b: a + b           # several arguments

list(map(fn, items))         # transform every item
list(filter(fn, items))      # keep items where fn(item) is True
sorted(items, key=fn)        # sort by what fn returns
sorted(items, reverse=True)  # descending
```

---

## Exercises

Run a file with `python exercises/<file>.py`, then compare with the matching
file in [`solutions/`](solutions/).

1. [`exercises/01_double_all.py`](exercises/01_double_all.py) — double every number with `map`.
2. [`exercises/02_filter_evens.py`](exercises/02_filter_evens.py) — keep the even numbers with `filter`.
3. [`exercises/03_sort_by_length.py`](exercises/03_sort_by_length.py) — sort words by length with `sorted`.

> Try each yourself **before** opening the solution.

---

Next → **15 · Modules & the Standard Library** _(coming soon)_
