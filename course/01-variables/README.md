# 01 · Variables

> **Part 1 — Fundamentals** · Estimated time: 20–30 min · No prior lessons required

A **variable** is a name you give to a value so you can use it again later.
Think of it as a labelled sticky note attached to a piece of data: the label is
the name, and the note points to the value.

## What you'll learn
- What a variable is and how to create one with `=`
- Why Python is *dynamically typed* (you never declare the type)
- How to reassign, update, and combine variables
- How to assign several variables at once and swap two values
- The **rules** (must follow) and **conventions** (should follow) for naming

---

## 1. Creating your first variable

You create a variable with a single equals sign, `=`. The name goes on the
**left**, the value goes on the **right**.

```python
name = "Ada"
age = 36

print(name)                       # Ada
print(f"{name} is {age} years old.")   # Ada is 36 years old.
```

That `f"..."` is an **f-string**. The `f` before the quotes lets you drop
variables straight into text using `{curly braces}`. You'll use f-strings
constantly — get comfortable with them now.

▶️ **Run it:** `python examples/01_first_variable.py`

---

## 2. Python figures out the type for you

In languages like Java or C++ you must announce a variable's type
(`int age = 36;`). Python doesn't — it looks at the value and works it out.
This is called **dynamic typing**.

```python
x = 100        # x is an integer right now
x = "hello"    # ...and now the SAME name points to a string. Totally fine.

print(type(x))     # <class 'str'>
```

`type(value)` tells you what kind of value a name currently points to. It's a
handy tool when something behaves unexpectedly.

▶️ **Run it:** `python examples/02_dynamic_typing.py`

> 💡 **Try it yourself:** make a variable `temperature = 21.5` and print
> `type(temperature)`. What does Python call a number with a decimal point?

---

## 3. Reassigning and updating

A variable can change as your program runs. You can even use a variable's
**old** value to compute its **new** value.

```python
score = 0
score = 10            # reassign to a brand-new value
score = score + 5     # use the old value to build the new one  -> 15
score += 5            # shorthand for "score = score + 5"        -> 20
```

The `+=` shortcut also has friends: `-=`, `*=`, `/=`.

▶️ **Run it:** `python examples/03_reassigning_and_updating.py`

---

## 4. Assigning many at once (and swapping)

```python
x, y, z = 10, 11, 12     # three names, three values, one line
a = b = c = 0            # give several names the same starting value

left, right = "L", "R"
left, right = right, left # swap two values in ONE line — a Python superpower
print(left, right)        # R L
```

▶️ **Run it:** `python examples/04_multiple_assignment_and_swapping.py`

---

## 5. Naming: rules vs. conventions

**Rules** — break these and Python raises an error:

- A name **cannot start with a digit**: `2cats` is invalid, `cats2` is fine.
- A name can only contain **letters, digits, and underscores** — no spaces,
  no hyphens, no symbols like `@`.
- Names are **case-sensitive**: `total` and `Total` are two different variables.

**Conventions** — Python still runs, but the community expects:

- Use **`snake_case`** for normal variables: `user_name`, `total_price`.
- Use **`UPPER_CASE`** for values you treat as constants: `MAX_SCORE = 100`.
- `CamelCase` is reserved for class names (you'll meet those in the OOP part).
- Names wrapped in double underscores like `__name__` are special to Python.
  **Don't invent your own.**

```python
user_name = "Sam"     # good
MAX_SCORE  = 100       # "constant" — by convention, don't change it
# 2cats = 10           # ❌ SyntaxError: can't start with a digit
# user-name = 10       # ❌ hyphen is not allowed
```

▶️ **Run it:** `python examples/05_naming.py`

---

## Common mistakes

| Mistake | What happens | Fix |
|---|---|---|
| `name = "Sam"` then later type `Name` | `NameError: name 'Name' is not defined` | Match the case exactly. |
| `2morrow = "day"` | `SyntaxError` | Start names with a letter: `tomorrow`. |
| Confusing `=` and `==` | `=` assigns; `==` compares | Use `=` to store, `==` to test equality (next lessons). |
| `print(f"Hi {name}")` but forgetting the `f` | prints the literal text `Hi {name}` | Add the `f` before the opening quote. |

---

## Recap / cheat-sheet

```python
name = "Ada"            # create
age = 36
age = 37               # reassign
age += 1               # update using the old value
x, y = 1, 2            # multiple assignment
x, y = y, x            # swap
type(name)             # inspect the current type
# snake_case for variables, UPPER_CASE for constants
```

---

## Exercises

Work through these in order. Each file explains the task at the top and has a
`TODO` where your code goes. Run a file with `python exercises/<file>.py`, then
compare with the matching file in [`solutions/`](solutions/) when you're done
(or stuck).

1. [`exercises/01_about_you.py`](exercises/01_about_you.py) — print a sentence about yourself with an f-string.
2. [`exercises/02_swap.py`](exercises/02_swap.py) — swap two values in one line.
3. [`exercises/03_rectangle.py`](exercises/03_rectangle.py) — compute a rectangle's area from variables.
4. [`exercises/04_fix_the_names.py`](exercises/04_fix_the_names.py) — debug some illegal variable names.

> Try each exercise yourself **before** opening the solution. Getting stuck and
> experimenting is where the learning happens.

---

Next → **02 · Data Types & Numbers** _(coming soon)_
