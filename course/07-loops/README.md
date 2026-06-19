# 07 · Loops

> **Part 1 — Fundamentals** · Estimated time: 30–40 min · Prerequisite: 06 · Conditionals

A **loop** repeats a block of code so you don't have to copy-paste it. Want to
greet 100 users, add up a column of numbers, or keep asking until the answer is
right? That's a loop. Python has two: the **`for`** loop (repeat once per item)
and the **`while`** loop (repeat as long as something stays true).

## What you'll learn
- `for` loops over a range of numbers and over the characters of a string
- The `range()` function with one, two, and three arguments
- `while` loops — and how to avoid the dreaded infinite loop
- `break` (stop early) and `continue` (skip to the next round)
- The accumulator pattern (building a running total)

---

## 1. The `for` loop

A `for` loop runs its body once for each item in a sequence.

```python
for number in range(1, 4):
    print(number)
# prints 1, then 2, then 3

for letter in "Hi":
    print(letter)
# prints H, then i
```

`number` and `letter` are just names *you* choose — they hold the current item
each time around. Like `if`, the body is **indented** under a line ending in `:`.

▶️ **Run it:** `python examples/01_for_loop.py`

---

## 2. The `range()` function

`range()` generates a sequence of numbers — perfect for counting.

```python
range(5)        # 0, 1, 2, 3, 4   (stop only: starts at 0, stops BEFORE 5)
range(1, 6)     # 1, 2, 3, 4, 5   (start, stop)
range(0, 10, 2) # 0, 2, 4, 6, 8   (start, stop, step)
```

The stop value is never included — `range(1, 6)` gives you 1 through 5.

▶️ **Run it:** `python examples/02_range_function.py`

> 💡 **Try it yourself:** print the even numbers from 2 to 10 using a single
> `range(...)`.

---

## 3. The `while` loop

A `while` loop keeps going **as long as** its condition is true.

```python
count = 1
while count <= 3:
    print(count)
    count += 1     # <-- without this, the loop never ends!
```

The danger: if the condition never becomes false, the loop runs forever. Always
make sure something inside the loop moves it toward stopping.

▶️ **Run it:** `python examples/03_while_loop.py`

---

## 4. `break` and `continue`

- **`break`** stops the loop immediately.
- **`continue`** skips the rest of this round and jumps to the next one.

```python
for n in range(1, 10):
    if n == 5:
        break        # stop entirely when we hit 5
    if n % 2 == 0:
        continue     # skip even numbers
    print(n)         # prints 1, 3
```

▶️ **Run it:** `python examples/04_break_and_continue.py`

---

## Common mistakes

| Mistake | What happens | Fix |
|---|---|---|
| `while` condition never goes false | infinite loop (program hangs) | Change something inside the loop (e.g. `count += 1`). |
| Expecting `range(1, 5)` to include 5 | it stops at 4 | Use `range(1, 6)` to reach 5. |
| Forgetting the `:` or indentation | `SyntaxError` / `IndentationError` | End the `for`/`while` line with `:` and indent the body. |
| Editing the counter in two places | hard-to-follow bugs | Update the loop variable in one obvious spot. |

---

## Recap / cheat-sheet

```python
for item in range(1, 6):   # 1..5
    print(item)

for char in "abc":         # loop over a string
    print(char)

range(stop)                # 0..stop-1
range(start, stop)         # start..stop-1
range(start, stop, step)   # ...stepping by step

count = 0
while count < 5:           # repeat while True
    count += 1             # move toward stopping!

break      # exit the loop now
continue   # skip to the next iteration
```

---

## Exercises

Run a file with `python exercises/<file>.py`, then compare with the matching
file in [`solutions/`](solutions/).

1. [`exercises/01_count_to_five.py`](exercises/01_count_to_five.py) — print 1 to 5 with a `for` loop.
2. [`exercises/02_sum_to_n.py`](exercises/02_sum_to_n.py) — add up 1..n with an accumulator.
3. [`exercises/03_countdown.py`](exercises/03_countdown.py) — count down with a `while` loop, then "Liftoff!".

> Try each yourself **before** opening the solution.

---

Next → **08 · Input & Output** _(coming soon)_
