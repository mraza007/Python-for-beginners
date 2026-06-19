# 04 · Booleans & Comparison

> **Part 1 — Fundamentals** · Estimated time: 20–30 min · Prerequisite: 02 · Data Types & Numbers

A **boolean** is a value that is either `True` or `False`. Booleans are how
programs answer yes/no questions — and answering questions is how programs make
decisions (which you'll do for real in the next lesson, Conditionals). Here we
learn how to *produce* `True`/`False` values by comparing and combining things.

## What you'll learn
- The two boolean values: `True` and `False`
- Comparison operators: `==`, `!=`, `<`, `>`, `<=`, `>=`
- Logical operators: `and`, `or`, `not`
- "Truthiness" — which everyday values count as `True` or `False`
- The classic `=` vs `==` mix-up

---

## 1. True and False

```python
is_open = True
is_raining = False
print(type(is_open))   # <class 'bool'>
```

Comparisons *produce* booleans — that's where they usually come from:

```python
print(10 > 3)     # True
print(2 == 5)     # False
```

▶️ **Run it:** `python examples/01_true_and_false.py`

---

## 2. Comparison operators

| Operator | Means | Example | Result |
|---|---|---|---|
| `==` | equal to | `5 == 5` | `True` |
| `!=` | not equal to | `5 != 3` | `True` |
| `>` | greater than | `5 > 8` | `False` |
| `<` | less than | `5 < 8` | `True` |
| `>=` | greater or equal | `5 >= 5` | `True` |
| `<=` | less or equal | `4 <= 3` | `False` |

> ⚠️ **`=` vs `==`:** a single `=` *assigns* a value (`x = 5`). A double `==`
> *compares* (`x == 5` asks "is x equal to 5?"). Mixing them up is the #1
> beginner bug.

▶️ **Run it:** `python examples/02_comparison_operators.py`

---

## 3. Logical operators: and / or / not

Combine yes/no answers into a bigger answer.

```python
print(True and False)   # False  -> and needs BOTH to be True
print(True or False)    # True   -> or needs only ONE to be True
print(not True)         # False  -> not flips it

age = 25
print(age >= 18 and age < 65)   # True  -> "an adult under 65"
```

▶️ **Run it:** `python examples/03_logical_operators.py`

> 💡 **Try it yourself:** write a comparison that is `True` only when a number
> `n` is **outside** the range 0–100 (less than 0 *or* more than 100).

---

## 4. Truthiness

Python can treat almost any value as a yes/no answer. These count as **falsy**
(act like `False`): `0`, `0.0`, `""` (empty string), `[]` (empty list), and
`None`. **Everything else is truthy.** `bool(value)` shows you which.

```python
print(bool(0))        # False
print(bool(""))       # False
print(bool("hi"))     # True
print(bool([]))       # False
print(bool([1, 2]))   # True
```

This is why you'll later see `if name:` meaning "if name isn't empty."

▶️ **Run it:** `python examples/04_truthiness.py`

---

## Common mistakes

| Mistake | What happens | Fix |
|---|---|---|
| `if x = 5:` | `SyntaxError` | Use `==` to compare: `x == 5`. |
| `True` vs `"True"` | the string `"True"` is just text (and always truthy) | Use the real keyword `True`, no quotes. |
| `1 < x < 10` confusion | actually this works in Python! | Chained comparisons are allowed and read naturally. |
| `not x == y` ambiguity | works, but clearer as `x != y` | Prefer `!=` for "not equal". |

---

## Recap / cheat-sheet

```python
True, False              # the two boolean values
a == b   a != b          # equal / not equal
a < b    a > b           # less / greater
a <= b   a >= b          # less-or-equal / greater-or-equal
a and b                  # both must be True
a or b                   # at least one True
not a                    # flip it
bool(value)              # truthy or falsy?
# falsy: 0, 0.0, "", [], None   (everything else is truthy)
```

---

## Exercises

Run a file with `python exercises/<file>.py`, then compare with the matching
file in [`solutions/`](solutions/).

1. [`exercises/01_can_vote.py`](exercises/01_can_vote.py) — turn an age into a True/False "can vote?" answer.
2. [`exercises/02_in_range.py`](exercises/02_in_range.py) — check whether a number sits inside a range.
3. [`exercises/03_truthy_or_falsy.py`](exercises/03_truthy_or_falsy.py) — predict and print the truthiness of several values.

> Try each yourself **before** opening the solution.

---

Next → **05 · Operators, Expressions & Statements** _(coming soon)_
