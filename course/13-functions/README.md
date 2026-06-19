# 13 · Functions

> **Part 3 — Functions & Modules** · Estimated time: 35–45 min · Prerequisite: 06 · Conditionals

A **function** is a named, reusable block of code. You define it once, then
*call* it whenever you need that job done — passing in **inputs** and getting
back an **output**. Functions keep your code **DRY** (Don't Repeat Yourself) and
let you break a big problem into small, named pieces.

## What you'll learn
- Defining a function with `def` and calling it
- **Parameters** (inputs) and `return` (output)
- The difference between a parameter and an argument
- **Default** values and **keyword** arguments
- Variable **scope** (local vs global) and writing **docstrings**
- Accepting any number of arguments with `*args`

---

## 1. Defining and calling

```python
def say_hi():
    print("Hi there!")

say_hi()      # call (invoke) the function
say_hi()      # call it again — reuse is the whole point
```

`def` starts the definition, the body is indented, and nothing runs until you
*call* it with `say_hi()`.

▶️ **Run it:** `python examples/01_defining_calling.py`

---

## 2. Parameters and return

A function can take **inputs** (parameters) and hand back a value with `return`.

```python
def square(num):
    return num * num

result = square(5)
print(result)      # 25
print(square(3))   # 9
```

> **Parameter vs argument:** in `def add(a, b)`, `a` and `b` are *parameters*. In
> `add(2, 4)`, the `2` and `4` are *arguments*. Order matters — `2` goes to `a`.

A function without `return` hands back `None`.

▶️ **Run it:** `python examples/02_parameters_and_return.py`

---

## 3. Default & keyword arguments

Give a parameter a **default** so callers can leave it out:

```python
def power(base, exponent=2):
    return base ** exponent

print(power(5))      # 25   (exponent defaults to 2)
print(power(5, 3))   # 125
```

Pass arguments **by name** (keyword arguments) for clarity and any order:

```python
print(power(exponent=3, base=2))   # 8
```

▶️ **Run it:** `python examples/03_default_and_keyword_arguments.py`

> 💡 **Try it yourself:** write `greet(name, greeting="Hello")` that returns
> `"Hello, Sam!"` by default but can say `"Hi, Sam!"` when asked.

---

## 4. Scope & docstrings

Variables created **inside** a function only exist there — that's its **local
scope**. A triple-quoted string just under `def` is a **docstring** that
documents the function.

```python
def add(x, y):
    """Return the sum of x and y."""
    result = x + y      # 'result' exists only inside add()
    return result

print(add(2, 3))     # 5
print(add.__doc__)   # Return the sum of x and y.
# print(result)      # NameError — 'result' isn't visible out here
```

▶️ **Run it:** `python examples/04_scope_and_docstrings.py`

---

## 5. Any number of arguments: `*args`

Prefix a parameter with `*` to gather *all* the extra arguments into a tuple.

```python
def total(*numbers):
    running = 0
    for n in numbers:
        running += n
    return running

print(total(1, 2, 3))         # 6
print(total(10, 20, 30, 40))  # 100
```

▶️ **Run it:** `python examples/05_flexible_args.py`

---

## Common mistakes

| Mistake | What happens | Fix |
|---|---|---|
| `return` indented inside the loop | exits on the first pass | Indent `return` to line up with the loop, not inside it. |
| Forgetting to **call** with `()` | nothing happens (you referenced the function object) | Call it: `say_hi()`. |
| Expecting a print to be a return | the caller gets `None` | Use `return` to send a value back. |
| Reading a local variable outside | `NameError` | Return it, or define it in the outer scope. |

---

## Recap / cheat-sheet

```python
def name(param1, param2=default):
    """Docstring describing the function."""
    return value

name(arg1, arg2)          # call with positional args
name(param2=x, param1=y)  # call with keyword args

def f(*args):  ...        # gather extra positional args into a tuple
def f(**kwargs): ...      # gather extra keyword args into a dict
```

---

## Exercises

Run a file with `python exercises/<file>.py`, then compare with the matching
file in [`solutions/`](solutions/).

1. [`exercises/01_greet.py`](exercises/01_greet.py) — write and call a `greet(name)` function.
2. [`exercises/02_rectangle_area.py`](exercises/02_rectangle_area.py) — return a computed value.
3. [`exercises/03_power_default.py`](exercises/03_power_default.py) — use a default parameter.

> Try each yourself **before** opening the solution.

---

Next → **14 · Lambdas & map/filter** _(coming soon)_
