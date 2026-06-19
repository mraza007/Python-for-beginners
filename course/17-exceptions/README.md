# 17 · Exceptions & Error Handling

> **Part 4 — Real-World Python** · Estimated time: 25–35 min · Prerequisite: 13 · Functions

When something goes wrong at runtime — bad input, a missing file, dividing by
zero — Python raises an **exception**. If you ignore it, your program crashes.
**Exception handling** lets you catch the problem, respond gracefully, and keep
going. This is what separates fragile scripts from robust programs.

## What you'll learn
- What an exception is and what an uncaught one does
- `try` / `except` to catch errors
- Catching **specific** exception types
- `else` and `finally`
- `raise`-ing your own exceptions

---

## 1. `try` / `except`

Wrap risky code in `try`. If it raises an exception, the matching `except` block
runs instead of crashing.

```python
try:
    number = int("abc")     # raises ValueError
    print(number)
except ValueError:
    print("That wasn't a valid number.")

print("The program keeps running.")
```

Without the `try`, `int("abc")` would stop the whole program.

▶️ **Run it:** `python examples/01_try_except.py`

---

## 2. Catch specific exceptions

Catch the exact kind of problem you expect — it's clearer and safer than
catching everything. You can grab the error object with `as`.

```python
def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "You can't divide by zero!"

print(divide(10, 2))   # 5.0
print(divide(10, 0))   # You can't divide by zero!

try:
    value = int("oops")
except (ValueError, TypeError) as e:   # catch more than one type
    print("Problem:", e)
```

Common built-in exceptions: `ValueError`, `TypeError`, `ZeroDivisionError`,
`KeyError`, `IndexError`, `FileNotFoundError`.

▶️ **Run it:** `python examples/02_specific_exceptions.py`

> 💡 **Try it yourself:** what exception does `[1, 2, 3][5]` raise? Catch it and
> print a friendly message.

---

## 3. `else` and `finally`

- `else` runs only if **no** exception happened.
- `finally` runs **no matter what** — perfect for cleanup.

```python
try:
    result = 10 / 2
except ZeroDivisionError:
    print("Division failed")
else:
    print("Success:", result)   # only when there was no error
finally:
    print("This always runs")   # always, error or not
```

▶️ **Run it:** `python examples/03_else_finally.py`

---

## 4. Raising your own exceptions

Use `raise` to signal that something is wrong — then callers can catch it.

```python
def set_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative")
    return age

try:
    set_age(-1)
except ValueError as e:
    print("Caught:", e)
```

▶️ **Run it:** `python examples/04_raising.py`

---

## Common mistakes

| Mistake | What happens | Fix |
|---|---|---|
| Bare `except:` catching everything | hides real bugs (even typos) | Catch specific types: `except ValueError:`. |
| Putting too much in the `try` | unclear which line failed | Keep only the risky line(s) inside `try`. |
| Using exceptions for normal flow | slow, confusing | Use `if` checks for expected cases. |
| Silently `pass`-ing in `except` | errors vanish without a trace | At least log or print what happened. |

---

## Recap / cheat-sheet

```python
try:
    risky()                 # code that might fail
except SomeError as e:
    handle(e)               # runs if that error occurs
except (ErrA, ErrB):
    ...                     # catch several types
else:
    ...                     # runs if NO exception
finally:
    cleanup()               # always runs

raise ValueError("message") # signal an error yourself
```

---

## Exercises

Run a file with `python exercises/<file>.py`, then compare with the matching
file in [`solutions/`](solutions/).

1. [`exercises/01_safe_divide.py`](exercises/01_safe_divide.py) — handle division by zero.
2. [`exercises/02_parse_int.py`](exercises/02_parse_int.py) — catch a `ValueError` from a bad conversion.
3. [`exercises/03_validate_age.py`](exercises/03_validate_age.py) — `raise` and catch your own error.

> Try each yourself **before** opening the solution.

---

Next → **18 · File Handling** _(coming soon)_
