# 15 · Modules & the Standard Library

> **Part 3 — Functions & Modules** · Estimated time: 25–35 min · Prerequisite: 13 · Functions

A **module** is just a Python file full of useful code you can reuse. Python
ships with a huge **standard library** of them (maths, random numbers, dates, and
more), and you can write your own. Importing modules means you rarely have to
build things from scratch.

## What you'll learn
- Importing modules with `import`
- The handy `import ... as` alias and `from ... import name` styles
- A taste of the standard library: `math` and `random`
- Writing and importing your **own** module
- The `if __name__ == "__main__"` pattern

---

## 1. Importing from the standard library

```python
import math

print(math.sqrt(16))   # 4.0
print(math.pi)         # 3.141592653589793
print(math.floor(3.7)) # 3
print(math.ceil(3.2))  # 4
```

Once imported, you reach inside the module with a dot: `math.sqrt`.

▶️ **Run it:** `python examples/01_import_stdlib.py`

---

## 2. Three ways to import

```python
import random            # the whole module
import math as m         # give it a shorter alias
from math import sqrt, pi  # pull specific names in directly

print(m.floor(2.9))   # 2
print(sqrt(25))       # 5.0   (no "math." needed — we imported it directly)
print(pi)             # 3.141592653589793
```

Use an alias for long names; use `from ... import` when you only need a couple of
things and want to type them without the prefix.

▶️ **Run it:** `python examples/02_import_styles.py`

> 💡 **Try it yourself:** `import random`, then `random.seed(0)` and print
> `random.randint(1, 6)`. (Seeding makes the "random" result repeat, which is
> handy for testing.)

---

## 3. Writing your own module

A module is *just a .py file*. The file [`examples/greetings.py`](examples/greetings.py)
defines two functions:

```python
# greetings.py
def hello():
    return "Hello!"

def hey(name):
    return f"Hey {name}!"
```

Another file imports it by filename (without the `.py`):

```python
import greetings

print(greetings.hello())     # Hello!
print(greetings.hey("Sam"))  # Hey Sam!
```

▶️ **Run it** (from the `examples/` folder): `python examples/03_use_custom_module.py`

---

## 4. `if __name__ == "__main__"`

When you run a file directly, Python sets its `__name__` to `"__main__"`. When
the file is *imported*, `__name__` is the module's name instead. This lets a file
include a demo that runs only when launched directly — not when imported:

```python
def hello():
    return "Hello!"

if __name__ == "__main__":
    print(hello())   # runs only via `python greetings.py`, not when imported
```

---

## Common mistakes

| Mistake | What happens | Fix |
|---|---|---|
| `import Math` | `ModuleNotFoundError` | Module names are lowercase: `import math`. |
| `sqrt(9)` without importing it | `NameError` | `from math import sqrt` first, or use `math.sqrt`. |
| Naming your file `random.py` | it shadows the real module | Don't name files after standard modules. |
| Expecting a module's demo to run on import | the `__main__` block is skipped | That's the point — guard demos with `if __name__ == "__main__"`. |

---

## Recap / cheat-sheet

```python
import math               # math.sqrt(16)
import math as m          # m.sqrt(16)
from math import sqrt     # sqrt(16)
from math import *        # import everything (use sparingly)

# your own module is just a .py file:
import greetings          # uses greetings.py in the same folder
greetings.hello()

if __name__ == "__main__":
    ...                   # runs only when this file is run directly
```

---

## Exercises

Run a file with `python exercises/<file>.py`, then compare with the matching
file in [`solutions/`](solutions/).

1. [`exercises/01_square_root.py`](exercises/01_square_root.py) — use `math.sqrt`.
2. [`exercises/02_circle_area.py`](exercises/02_circle_area.py) — use `math.pi`.
3. [`exercises/03_from_import.py`](exercises/03_from_import.py) — import a single name with `from`.

> Try each yourself **before** opening the solution.

---

Next → **16 · Iterators & Generators** _(coming soon)_
