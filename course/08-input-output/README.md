# 08 · Input & Output

> **Part 1 — Fundamentals** · Estimated time: 20–30 min · Prerequisite: 02 · Data Types & Numbers

So far your programs have only talked *to* you with `print()`. Now they'll listen
*back* with `input()`. This is what makes a program interactive — it can ask a
question, take an answer, and respond. We'll also polish how `print()` displays
things.

## What you'll learn
- `print()` with several values, plus the `sep=` and `end=` options
- `input()` — and the crucial fact that **it always returns a string**
- Converting input to numbers with `int()` / `float()`
- Formatting numbers neatly in f-strings (decimals, percentages, alignment)

> ℹ️ These programs are **interactive** — when you run them, type your answer and
> press Enter. Each interactive example's docstring also shows how to feed input
> automatically with `printf '...' | python file.py` if you'd like.

---

## 1. Printing, with options

```python
print("a", "b", "c")            # a b c   (print puts spaces between values)
print("a", "b", "c", sep="-")   # a-b-c   (sep changes the separator)
print("Loading", end="...")     # no line break yet
print("done")                   # Loading...done
```

By default `print()` adds a space between values and a newline at the end. `sep=`
and `end=` let you change both.

▶️ **Run it:** `python examples/01_print_options.py`

---

## 2. Reading input

```python
name = input("What is your name? ")   # shows the prompt, waits for Enter
print(f"Hello, {name}!")
```

`input()` shows your prompt, waits for the user to type a line, and hands it back
**as a string** — always, even if they typed digits.

▶️ **Run it** (then type your answer): `python examples/02_getting_input.py`

---

## 3. Input is text — convert it for maths

Because `input()` gives you a string, `"5" + "3"` would be `"53"`, not `8`. To do
maths, convert first with `int()` or `float()`.

```python
age_text = input("How old are you? ")   # e.g. "20" (a string)
age = int(age_text)                     # 20 (a number)
print(f"Next year you'll be {age + 1}.")
```

▶️ **Run it** (then type a number): `python examples/03_input_numbers.py`

> 💡 **Try it yourself:** ask for a price as a `float`, then print it doubled.

---

## 4. Formatting numbers in f-strings

Put a `:` after the value inside the braces to control how it looks.

```python
price = 3.14159
print(f"{price:.2f}")    # 3.14   two decimal places
ratio = 0.25
print(f"{ratio:.0%}")    # 25%    as a percentage
name = "Sam"
print(f"|{name:<8}|")    # |Sam     |   left-aligned in 8 spaces
print(f"|{name:>8}|")    # |     Sam|   right-aligned
```

▶️ **Run it:** `python examples/04_formatting.py`

---

## Common mistakes

| Mistake | What happens | Fix |
|---|---|---|
| `input() + 1` | `TypeError` (string + int) | Convert first: `int(input(...)) + 1`. |
| `"5" + "3"` expecting `8` | gives `"53"` (text joined) | Convert both to numbers before adding. |
| `int(input("Age: "))` and user types "abc" | `ValueError` | Ask for a number; (handling bad input nicely comes in the Exceptions lesson). |
| Forgetting the prompt text | user sees a blank cursor | Pass a prompt string: `input("Name: ")`. |

---

## Recap / cheat-sheet

```python
print(a, b, c)               # a b c
print(a, b, sep=", ")        # a, b
print("x", end="")           # no trailing newline

text = input("Prompt: ")     # ALWAYS a string
number = int(input("n: "))   # convert for maths
price = float(input("$: "))

f"{value:.2f}"               # 2 decimals
f"{value:.0%}"               # percentage
f"{text:<10}" / f"{text:>10}"  # left / right align
```

---

## Exercises

These exercises are interactive. Run with `python exercises/<file>.py` and type
your answers, then compare with the matching file in [`solutions/`](solutions/).
Each docstring shows a **Sample run** (the parts *you* type are after each prompt).

1. [`exercises/01_greeting.py`](exercises/01_greeting.py) — ask for a name and greet the user.
2. [`exercises/02_add_two_numbers.py`](exercises/02_add_two_numbers.py) — add two numbers the user enters.
3. [`exercises/03_rectangle_area.py`](exercises/03_rectangle_area.py) — ask for width and height, print the area.

> Try each yourself **before** opening the solution.

---

Next → **09 · Lists** _(coming soon)_
