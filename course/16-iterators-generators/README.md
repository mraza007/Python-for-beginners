# 16 · Iterators & Generators

> **Part 3 — Functions & Modules** · Estimated time: 25–35 min · Prerequisite: 12 · Comprehensions

Ever wondered how a `for` loop actually walks through a list? The answer is
**iterators**. And **generators** are a wonderfully simple way to *create* your
own sequences — even huge or never-ending ones — without storing them all in
memory at once. This lesson demystifies both.

## What you'll learn
- The difference between an **iterable** and an **iterator** (`iter`, `next`)
- What a `for` loop is really doing under the hood
- Writing a **generator** function with `yield`
- **Generator expressions** — comprehensions that don't build a list
- Why generators are **lazy** and memory-friendly

---

## 1. Iterables and iterators

An **iterable** is anything you can loop over (a list, string, range…). Calling
`iter()` on it gives you an **iterator**, and `next()` pulls one item at a time.

```python
colors = ["red", "green", "blue"]
it = iter(colors)        # turn the iterable into an iterator

print(next(it))   # red
print(next(it))   # green
print(next(it))   # blue
# next(it)        # StopIteration — there's nothing left
```

A `for` loop does all of this for you: it calls `iter()`, then `next()` over and
over, and stops cleanly when `StopIteration` happens.

▶️ **Run it:** `python examples/01_iter_next.py`

---

## 2. Generator functions (`yield`)

A **generator** is a function that uses `yield` instead of `return`. Each `yield`
hands back one value and **pauses** the function until the next value is
requested.

```python
def count_up(limit):
    n = 1
    while n <= limit:
        yield n        # produce n, then pause right here
        n += 1

print(list(count_up(5)))   # [1, 2, 3, 4, 5]

for value in count_up(3):
    print(value)           # 1, 2, 3
```

▶️ **Run it:** `python examples/02_generator_function.py`

> 💡 **Try it yourself:** write a generator `evens(limit)` that yields the even
> numbers up to `limit`.

---

## 3. Generator expressions

These look exactly like list comprehensions, but with **parentheses** instead of
square brackets. They produce items on demand rather than building a whole list.

```python
squares = (n * n for n in range(1, 6))
print(squares)         # <generator object ...>  (nothing computed yet)
print(list(squares))   # [1, 4, 9, 16, 25]

# Perfect with sum()/max() — no intermediate list is created:
print(sum(n * n for n in range(1, 6)))   # 55
```

▶️ **Run it:** `python examples/03_generator_expression.py`

---

## 4. Lazy = memory-friendly

Because generators compute values only when asked, they can represent enormous —
even infinite — sequences cheaply.

```python
def naturals():
    n = 1
    while True:        # this would be an infinite list, but a generator is fine
        yield n
        n += 1

for value in naturals():
    if value > 5:
        break
    print(value)       # 1, 2, 3, 4, 5
```

▶️ **Run it:** `python examples/04_why_lazy.py`

---

## Common mistakes

| Mistake | What happens | Fix |
|---|---|---|
| Reusing an exhausted iterator/generator | it yields nothing the second time | Create a fresh one, or collect into a `list` first. |
| `return value` inside a generator | ends the generator (doesn't yield) | Use `yield` to produce values. |
| `print(my_generator)` | shows `<generator object …>` | Wrap it: `print(list(my_generator))`. |
| Looping an infinite generator with no `break` | runs forever | Always have a stopping condition. |

---

## Recap / cheat-sheet

```python
it = iter(iterable)      # iterable -> iterator
next(it)                 # next item (StopIteration when done)

def gen(n):              # generator function
    for i in range(n):
        yield i          # produce a value, then pause

(x * x for x in xs)      # generator expression (lazy)
list(gen(3))             # collect all values
```

---

## Exercises

Run a file with `python exercises/<file>.py`, then compare with the matching
file in [`solutions/`](solutions/).

1. [`exercises/01_manual_iteration.py`](exercises/01_manual_iteration.py) — step through with `iter`/`next`.
2. [`exercises/02_countdown_generator.py`](exercises/02_countdown_generator.py) — write a generator with `yield`.
3. [`exercises/03_squares_genexp.py`](exercises/03_squares_genexp.py) — total squares with a generator expression.

> Try each yourself **before** opening the solution.

---

Next → **17 · Exceptions & Error Handling** _(coming soon)_
