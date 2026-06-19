# 19 · Debugging

> **Part 4 — Real-World Python** · Estimated time: 25–35 min · Prerequisite: 17 · Exceptions & Error Handling

Every programmer writes bugs — debugging is the skill of *finding and fixing*
them, and it's just as important as writing code. The good news: Python's error
messages are genuinely helpful once you know how to read them. This lesson is
about staying calm and systematic when something breaks.

## What you'll learn
- The most common Python errors and what each one means
- How to read a **traceback** (hint: from the bottom up)
- **Print debugging** — the simplest, most useful tool
- The built-in interactive debugger (`breakpoint()`)
- A calm, repeatable approach to fixing bugs

---

## 1. Common errors and what they mean

| Error | Usually means | Typical fix |
|---|---|---|
| `SyntaxError` | Python can't parse the code | Check for a missing `:`, `)`, or quote. |
| `NameError` | a name isn't defined (often a typo) | Check spelling / that it's defined first. |
| `TypeError` | wrong type for an operation | e.g. don't add `str + int` — convert first. |
| `IndexError` | list index out of range | Valid indexes are `0`..`len-1`. |
| `KeyError` | dictionary has no such key | Use `.get()` or check `in` first. |
| `ValueError` | right type, wrong value | e.g. `int("abc")`. |
| `AttributeError` | object has no such attribute/method | Check the object's type and method name. |

```python
try:
    print([1, 2, 3][10])
except IndexError as e:
    print("IndexError:", e)
```

▶️ **Run it:** `python examples/01_common_errors.py`

---

## 2. Reading a traceback

When code crashes, Python prints a **traceback**. Read it **bottom-up**: the last
line is the actual error and message; the lines above show the chain of calls
that led there, with file names and line numbers.

```python
import traceback

def step_three(): return 1 / 0
def step_two():   return step_three()
def step_one():   return step_two()

try:
    step_one()
except ZeroDivisionError:
    traceback.print_exc()   # shows the same traceback you'd see on a crash
```

The bottom line says `ZeroDivisionError: division by zero`, and just above it
you'll see it happened in `step_three`. That's your starting point.

▶️ **Run it:** `python examples/02_reading_traceback.py`

> 💡 **Try it yourself:** what's the very first thing you should look at in a
> traceback? (The bottom line — the error type and message.)

---

## 3. Print debugging

The fastest way to understand what your code is *actually* doing is to print
values as it runs. Add temporary `print()` calls, see what's happening, then
remove them.

```python
def double_all(numbers):
    result = []
    for n in numbers:
        print(f"DEBUG: processing {n}")   # temporary — watch the loop
        result.append(n * 2)
    return result

print(double_all([1, 2, 3]))
```

▶️ **Run it:** `python examples/03_print_debugging.py`

---

## 4. The interactive debugger

For trickier bugs, Python's built-in debugger lets you pause and inspect. Add
`breakpoint()` where you want to stop, then run the file normally:

```python
def buggy(x):
    breakpoint()    # execution pauses here and gives you a (Pdb) prompt
    return x * 2
```

At the `(Pdb)` prompt:

| Command | Does |
|---|---|
| `p name` | **p**rint a variable's value |
| `n` | run the **n**ext line |
| `c` | **c**ontinue until the next breakpoint or the end |
| `l` | **l**ist the code around the current line |
| `q` | **q**uit the debugger |

(The debugger is interactive, so it isn't runnable in the in-browser version —
try it in a terminal.)

---

## A calm debugging method

1. **Read the error** — the bottom of the traceback tells you *what* and *where*.
2. **Reproduce it** — make the bug happen reliably.
3. **Inspect** — print the values right before the failing line. Are they what
   you expected?
4. **Form one hypothesis, test it** — change one thing at a time.
5. **Fix, then re-run** — confirm it's gone, and that you didn't break anything else.

---

## Common mistakes

| Mistake | What happens | Fix |
|---|---|---|
| Panicking at a red wall of text | you miss the useful line | Read the **bottom** line first. |
| Changing many things at once | you can't tell what fixed it | Change one thing, re-run, repeat. |
| Ignoring the line number | you look in the wrong place | The traceback names the exact file and line. |
| Leaving debug prints in | noisy output | Remove them once the bug is fixed. |

---

## Recap / cheat-sheet

```python
# Read tracebacks bottom-up: last line = the error.
# Common errors: SyntaxError, NameError, TypeError, IndexError, KeyError, ValueError

print(f"DEBUG: x = {x}")   # print-debugging

breakpoint()               # drop into the interactive debugger
# (Pdb) p x   n   c   l   q
```

---

## Exercises

Each file below has a bug. Read the comment, fix the code so it produces the
expected output, then check against [`solutions/`](solutions/).

1. [`exercises/01_fix_the_nameerror.py`](exercises/01_fix_the_nameerror.py) — squash a `NameError`.
2. [`exercises/02_fix_the_indexerror.py`](exercises/02_fix_the_indexerror.py) — fix an `IndexError`.
3. [`exercises/03_fix_the_typeerror.py`](exercises/03_fix_the_typeerror.py) — fix a `TypeError`.

> Try each yourself **before** opening the solution.

---

Next → **20 · Classes & Objects** _(coming soon)_
