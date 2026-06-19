# 03 · Strings

> **Part 1 — Fundamentals** · Estimated time: 25–35 min · Prerequisite: 02 · Data Types & Numbers

A **string** is text — a "string" of characters like `"Hello"`. Strings are
everywhere: names, messages, file contents, user input. This lesson shows how to
create them, join them, pull pieces out of them, and transform them with
built-in methods.

## What you'll learn
- Creating strings with single, double, and triple quotes
- Joining strings with `+`, `+=`, and (best of all) f-strings
- Measuring length with `len()` and reading characters by **index**
- **Slicing** out a piece of a string
- Handy string methods: `.upper()`, `.lower()`, `.strip()`, `.replace()`, `.split()`, `.join()`
- Why strings are **immutable**

---

## 1. Creating strings

```python
single = 'Hello'
double = "Hello"          # single and double quotes both work
sentence = "It's fine"    # use double quotes when the text has an apostrophe

paragraph = """This string
spans multiple lines."""  # triple quotes keep line breaks

print(len(single))        # 5  -> number of characters
```

▶️ **Run it:** `python examples/01_creating_strings.py`

---

## 2. Joining strings

```python
first = "Hello"
second = "World"
print(first + " " + second)   # Hello World   (+ glues strings together)

greeting = "Hi"
greeting += "!"               # += appends
print(greeting)               # Hi!
```

The cleanest way to build text from variables is an **f-string**:

```python
name = "Ada"
age = 36
print(f"{name} is {age} years old.")   # Ada is 36 years old.
```

You can't glue text to a number directly (`"age: " + 36` is an error) — but an
f-string converts for you automatically. If you ever do need it as text, use
`str(36)`.

▶️ **Run it:** `python examples/02_concatenation_and_fstrings.py`

---

## 3. Indexing and slicing

Each character has a position (an **index**) starting at `0`. Negative indexes
count from the end.

```python
word = "Python"
print(word[0])    # P   (first character)
print(word[-1])   # n   (last character)

print(word[0:3])  # Pyt  (slice: from index 0 up to — but not including — 3)
print(word[3:])   # hon  (from index 3 to the end)
print(word[:2])   # Py   (from the start up to index 2)
```

▶️ **Run it:** `python examples/03_indexing_and_slicing.py`

> 💡 **Try it yourself:** given `word = "Python"`, can you print just `"tho"`
> using a slice?

---

## 4. Useful string methods (and immutability)

A **method** is a function attached to a value; you call it with a dot.

```python
text = "  Hello World  "
print(text.upper())        # "  HELLO WORLD  "
print(text.lower())        # "  hello world  "
print(text.strip())        # "Hello World"  (trims spaces at both ends)
print(text.replace("o", "0"))   # "  Hell0 W0rld  "
print("a,b,c".split(","))  # ['a', 'b', 'c']  -> a list
print("-".join(["a", "b", "c"]))  # "a-b-c"
```

Strings are **immutable** — methods return a *new* string and never change the
original. `word[0] = "J"` is an error.

▶️ **Run it:** `python examples/04_string_methods.py`

---

## Common mistakes

| Mistake | What happens | Fix |
|---|---|---|
| `"age: " + 36` | `TypeError` | Use an f-string, or `str(36)`. |
| `word[6]` on `"Python"` | `IndexError` (valid indexes are 0–5) | Remember indexing starts at 0; last is `len-1` or `-1`. |
| Expecting `text.strip()` to change `text` | `text` is unchanged | Strings are immutable — save the result: `text = text.strip()`. |
| `'It's fine'` | `SyntaxError` (the apostrophe ends the string) | Use double quotes: `"It's fine"`. |

---

## Recap / cheat-sheet

```python
s = "Hello"
len(s)            # 5
s[0]              # 'H'   first character
s[-1]             # 'o'   last character
s[1:4]            # 'ell' slice [start:stop]
s + " there"      # join with +
f"{name} is {n}"  # f-string (preferred)
s.upper() / s.lower() / s.strip()
s.replace("l", "L")
"a,b".split(",")  # -> ['a', 'b']
",".join(parts)   # list -> string
```

---

## Exercises

Run a file with `python exercises/<file>.py`, then compare with the matching
file in [`solutions/`](solutions/).

1. [`exercises/01_full_name.py`](exercises/01_full_name.py) — build a full name and report its length.
2. [`exercises/02_initials.py`](exercises/02_initials.py) — extract initials using indexing.
3. [`exercises/03_clean_username.py`](exercises/03_clean_username.py) — tidy a messy username with `.strip()` and `.lower()`.

> Try each yourself **before** opening the solution.

---

Next → **04 · Booleans & Comparison** _(coming soon)_
