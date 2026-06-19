# 05 · Operators, Expressions & Statements

> **Part 1 — Fundamentals** · Estimated time: 20–30 min · Prerequisite: 04 · Booleans & Comparison

You've already used `+`, `=`, and `==`. This lesson names the building blocks
properly: an **expression** produces a value, a **statement** performs an
action, and **operators** are the symbols that do the work. Understanding
**operator precedence** (the order Python applies them) saves you from a whole
class of silent bugs.

## What you'll learn
- The difference between an **expression** and a **statement**
- The arithmetic operators and **augmented assignment** (`+=`, `-=`, …)
- **Operator precedence** and how parentheses control it
- Using `+` and `*` with strings

---

## 1. Expressions vs. statements

An **expression** is anything that evaluates to a value:

```python
3 + 4            # evaluates to 7
"Hi " + "there"  # evaluates to "Hi there"
age >= 18        # evaluates to True or False
```

A **statement** does something — like assigning a variable or printing:

```python
x = 3 + 4        # assignment statement (it contains the expression 3 + 4)
print(x)         # a statement that performs an action
```

Rule of thumb: if you could put it on the right of an `=`, it's an expression.

▶️ **Run it:** `python examples/01_expressions_vs_statements.py`

---

## 2. Arithmetic & augmented assignment

```python
print(10 + 3, 10 - 3, 10 * 3)   # 13 7 30
print(10 / 3)    # 3.33...  (always a float)
print(10 // 3)   # 3        (floor division)
print(10 % 3)    # 1        (remainder)
print(2 ** 4)    # 16       (power)
```

**Augmented assignment** updates a variable using its own value:

```python
total = 0
total += 5     # same as total = total + 5
total *= 2     # same as total = total * 2
print(total)   # 10
```

▶️ **Run it:** `python examples/02_arithmetic_operators.py`

---

## 3. Operator precedence (order of operations)

Python follows maths rules (think **PEMDAS**): `**` first, then `*` `/` `//`
`%`, then `+` `-`. **Parentheses** override everything — when in doubt, add them.

```python
print(2 + 3 * 4)     # 14  (multiplication happens first)
print((2 + 3) * 4)   # 20  (parentheses force the addition first)
print(10 - 2 - 3)    # 5   (left to right)
```

▶️ **Run it:** `python examples/03_operator_precedence.py`

> 💡 **Try it yourself:** what does `8 / 2 + 2` give? What about `8 / (2 + 2)`?
> Predict, then check.

---

## 4. Operators on strings

`+` joins strings; `*` repeats them.

```python
print("ab" + "cd")   # abcd
print("ha" * 3)      # hahaha
print("-" * 10)      # ----------  (great for separator lines)
```

▶️ **Run it:** `python examples/04_string_operators.py`

---

## Common mistakes

| Mistake | What happens | Fix |
|---|---|---|
| `2 + 3 * 4` expecting `20` | gives `14` — `*` binds tighter than `+` | Add parentheses: `(2 + 3) * 4`. |
| `"5" * "3"` | `TypeError` | `*` repeats a string by an **int**, e.g. `"5" * 3`. |
| Writing `x =+ 1` | sets `x` to `+1`, not "add 1" | The operator is `+=`, not `=+`. |
| Relying on remembered precedence | subtle bugs | When unsure, just use parentheses. |

---

## Recap / cheat-sheet

```python
# expression -> a value;  statement -> an action
+  -  *  /  //  %  **      # arithmetic
+=  -=  *=  /=            # augmented assignment
# precedence: ()  >  **  >  * / // %  >  + -
"a" + "b"                 # join strings
"ab" * 3                  # repeat strings
```

---

## Exercises

Run a file with `python exercises/<file>.py`, then compare with the matching
file in [`solutions/`](solutions/).

1. [`exercises/01_fix_precedence.py`](exercises/01_fix_precedence.py) — add parentheses so an average comes out right.
2. [`exercises/02_receipt_bar.py`](exercises/02_receipt_bar.py) — use string repetition to draw a separator.
3. [`exercises/03_celsius_to_fahrenheit.py`](exercises/03_celsius_to_fahrenheit.py) — apply a formula with correct precedence.

> Try each yourself **before** opening the solution.

---

Next → **06 · Conditionals** _(coming soon)_
