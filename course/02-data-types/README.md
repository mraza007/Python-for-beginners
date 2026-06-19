# 02 · Data Types & Numbers

> **Part 1 — Fundamentals** · Estimated time: 20–30 min · Prerequisite: 01 · Variables

Every value in Python has a **type** — a category that tells Python what the
value is and what you can do with it. A whole number, a word, a yes/no flag, and
a decimal are all different types. This lesson tours the core types and shows how
to do maths and convert between them.

## What you'll learn
- The core built-in types: `int`, `float`, `str`, `bool` (and `None`)
- How to inspect a value's type with `type()`
- Whole-number vs decimal maths, and the operators `//`, `%`, `**`
- How to convert between types with `int()`, `float()`, `str()`
- The classic "input is always text" trap and how to avoid it

---

## 1. The core data types

```python
age = 36           # int   — a whole number
price = 9.99       # float — a number with a decimal point
name = "Ada"       # str   — text (a "string" of characters)
is_member = True   # bool  — a yes/no value: True or False
nothing = None     # NoneType — "no value here yet"
```

`type(value)` tells you which type a value is — handy when something misbehaves.

```python
print(type(age))    # <class 'int'>
print(type(price))  # <class 'float'>
print(type(name))   # <class 'str'>
```

▶️ **Run it:** `python examples/01_core_types.py`

---

## 2. Doing maths with numbers

Python has two number types: `int` (whole) and `float` (decimal). The usual
operators work, plus three you may not have seen:

```python
print(7 + 3)    # 10   addition
print(7 - 3)    # 4    subtraction
print(7 * 3)    # 21   multiplication
print(7 / 3)    # 2.333...  TRUE division — always gives a float
print(7 // 3)   # 2    FLOOR division — drops the remainder
print(7 % 3)    # 1    MODULO — just the remainder ("what's left over")
print(2 ** 3)   # 8    EXPONENT — 2 to the power of 3
```

`%` (modulo) is surprisingly useful: `n % 2 == 0` tells you `n` is even.

▶️ **Run it:** `python examples/02_numbers_arithmetic.py`

> 💡 **Try it yourself:** use `//` and `%` to work out how many whole weeks and
> leftover days are in `45` days. (Hint: there are 7 days in a week.)

---

## 3. Converting between types

You'll often need to turn one type into another. Python gives you a function
named after each type:

```python
int("42")     # 42    text -> whole number
float("3.14") # 3.14  text -> decimal
str(100)      # "100" number -> text
int(3.9)      # 3     float -> int (chops off the decimal, does NOT round)
round(3.9)    # 4     proper rounding (this one rounds)
```

This matters because **`input()` always gives you a string**, even if the user
types a number. To do maths with it you must convert first:

```python
text = "5"
# text + 1            # ❌ TypeError: can't add str and int
number = int(text)
print(number + 1)     # 6  ✅
```

▶️ **Run it:** `python examples/03_type_conversion.py`

---

## 4. `None` — the "nothing yet" value

`None` is Python's way of saying "no value." It is its own type and is not the
same as `0` or `""` (an empty string).

```python
winner = None         # we don't know the winner yet
print(winner)         # None
print(type(winner))   # <class 'NoneType'>
```

▶️ **Run it:** `python examples/04_none_value.py`

---

## Common mistakes

| Mistake | What happens | Fix |
|---|---|---|
| `"5" + 1` | `TypeError` | Convert first: `int("5") + 1`. |
| Expecting `7 / 2` to be `3` | It's `3.5` — `/` always returns a float | Use `//` for whole-number division. |
| `int(3.9)` to "round" | Gives `3`, not `4` (it chops) | Use `round(3.9)` to round. |
| `int("3.5")` | `ValueError` — `int()` won't parse a decimal string | Use `float("3.5")` first. |

---

## Recap / cheat-sheet

```python
type(value)        # what type is this?
int, float, str, bool, None   # the core types

a / b              # true division (float)
a // b             # floor division (drops remainder)
a % b              # remainder (modulo)
a ** b             # power

int("42")          # text  -> int
float("3.14")      # text  -> float
str(100)           # value -> text
round(3.9)         # 4 (real rounding)
```

---

## Exercises

Run a file with `python exercises/<file>.py`, then compare with the matching
file in [`solutions/`](solutions/).

1. [`exercises/01_identify_types.py`](exercises/01_identify_types.py) — print the type of several values.
2. [`exercises/02_seconds_to_time.py`](exercises/02_seconds_to_time.py) — split seconds into hours/minutes/seconds with `//` and `%`.
3. [`exercises/03_price_total.py`](exercises/03_price_total.py) — turn text prices into numbers and total them.

> Try each yourself **before** opening the solution.

---

Next → **03 · Strings** _(coming soon)_
