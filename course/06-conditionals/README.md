# 06 · Conditionals

> **Part 1 — Fundamentals** · Estimated time: 25–35 min · Prerequisite: 04 · Booleans & Comparison

A **conditional** lets your program make decisions: *if* something is true, do
one thing; *otherwise*, do another. This is where code stops being a fixed list
of steps and starts to react. You already know how to make `True`/`False`
values — now you'll act on them.

## What you'll learn
- The `if` statement, and why **indentation** and the **colon** matter
- Adding an `else` for the "otherwise" case
- Chaining choices with `elif`
- Combining conditions with `and` / `or` / `not`
- The one-line conditional expression (`a if condition else b`)

---

## 1. The `if` statement

```python
temperature = 30

if temperature > 25:
    print("It's warm out.")
    print("Wear a t-shirt.")
```

Two things are essential:
- the line ends with a **colon** `:`
- the body is **indented** (4 spaces). The indentation is how Python knows which
  lines belong "inside" the `if`. Lines that aren't indented run regardless.

▶️ **Run it:** `python examples/01_first_if.py`

---

## 2. `else` — the otherwise case

```python
age = 16

if age >= 18:
    print("You may enter.")
else:
    print("Sorry, 18 and over only.")
```

Exactly one of the two blocks runs — never both.

▶️ **Run it:** `python examples/02_if_else.py`

---

## 3. `elif` — choosing between many options

`elif` (short for "else if") lets you check several conditions in order. Python
runs the **first** one that's true and skips the rest.

```python
score = 85

if score >= 90:
    print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
else:
    print("F")
```

Order matters: because `85 >= 80` is checked before `85 >= 70`, you get `B`.

▶️ **Run it:** `python examples/03_elif_chain.py`

> 💡 **Try it yourself:** change `score` to `72` and predict the output before
> running it.

---

## 4. Combining conditions

Use `and`, `or`, `not` to build richer tests. You can also nest an `if` inside
another.

```python
age = 25
has_ticket = True

if age >= 18 and has_ticket:
    print("Enjoy the show!")

# A one-line conditional expression for simple either/or values:
weather = "rain"
plan = "stay in" if weather == "rain" else "go out"
print(plan)   # stay in
```

▶️ **Run it:** `python examples/04_combining_conditions.py`

---

## Common mistakes

| Mistake | What happens | Fix |
|---|---|---|
| Forgetting the `:` | `SyntaxError` | End the `if`/`elif`/`else` line with a colon. |
| Inconsistent indentation | `IndentationError` | Indent the body by 4 spaces, consistently. |
| `if x = 5:` | `SyntaxError` | Compare with `==`, not `=`. |
| Using many `if`s instead of `elif` | every condition is checked; more than one block can run | Use `elif` when the cases are alternatives. |

---

## Recap / cheat-sheet

```python
if condition:
    ...            # runs when condition is True
elif other:
    ...            # checked only if the ones above were False
else:
    ...            # runs when nothing above matched

# combine: if a and b:  / if a or b:  / if not a:
value = x if condition else y    # one-line conditional expression
```

---

## Exercises

Run a file with `python exercises/<file>.py`, then compare with the matching
file in [`solutions/`](solutions/).

1. [`exercises/01_even_or_odd.py`](exercises/01_even_or_odd.py) — decide if a number is even or odd.
2. [`exercises/02_grade.py`](exercises/02_grade.py) — turn a score into a letter grade with an `elif` chain.
3. [`exercises/03_ticket_price.py`](exercises/03_ticket_price.py) — pick a ticket price based on age.

> Try each yourself **before** opening the solution.

---

Next → **07 · Loops** _(coming soon)_
