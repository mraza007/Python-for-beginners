# 18 · File Handling

> **Part 4 — Real-World Python** · Estimated time: 25–35 min · Prerequisite: 07 · Loops

Programs become genuinely useful when they can **save** and **load** data —
notes, scores, settings, logs. Python reads and writes files with the `open()`
function and the `with` statement. This lesson covers writing, reading,
appending, and handling a missing file.

> ℹ️ Every example below cleans up after itself (it deletes the file it made), so
> running them won't litter your folder. In the in-browser version, files live in
> a temporary sandbox and vanish when you reload.

## What you'll learn
- Opening files with `open()` and the safe `with` statement
- Writing (`"w"`), reading (`"r"`), and appending (`"a"`)
- Reading a file line by line
- Handling a missing file with `FileNotFoundError`

---

## 1. Write and read

The `with open(...)` statement opens a file and **automatically closes it** when
the block ends. Mode `"w"` writes (creating or overwriting); mode `"r"` reads.

```python
with open("sample.txt", "w") as f:
    f.write("Hello, file!\n")
    f.write("Second line.\n")

with open("sample.txt", "r") as f:   # "r" is the default mode
    contents = f.read()
print(contents)
```

▶️ **Run it:** `python examples/01_write_and_read.py`

---

## 2. Read line by line

Looping over a file gives you one line at a time — memory-friendly for big files.
Each line keeps its trailing newline, so `.strip()` is handy.

```python
with open("fruits.txt") as f:
    for line in f:
        print(line.strip())
```

▶️ **Run it:** `python examples/02_reading_lines.py`

> 💡 **Try it yourself:** read a file into a list of lines with `f.readlines()`
> and print how many there are.

---

## 3. Append instead of overwrite

Mode `"w"` erases the file first. Mode `"a"` **appends** to the end, keeping
what's already there.

```python
with open("log.txt", "w") as f:
    f.write("line 1\n")
with open("log.txt", "a") as f:   # add without erasing
    f.write("line 2\n")
```

▶️ **Run it:** `python examples/03_append.py`

---

## 4. Handling a missing file

Opening a file that doesn't exist for reading raises `FileNotFoundError`. Catch
it (you met `try`/`except` in the previous lesson):

```python
try:
    with open("missing.txt") as f:
        print(f.read())
except FileNotFoundError:
    print("That file doesn't exist yet.")
```

▶️ **Run it:** `python examples/04_missing_file.py`

---

## Common mistakes

| Mistake | What happens | Fix |
|---|---|---|
| Opening with `"w"` to *keep* old data | the file is wiped first | Use `"a"` to append. |
| Forgetting to close the file | data may not be saved | Use `with open(...)` — it closes for you. |
| Reading a missing file | `FileNotFoundError` | Wrap it in `try`/`except`, or check it exists. |
| Expecting lines without `\n` | each line keeps its newline | Use `line.strip()` when printing. |

---

## Recap / cheat-sheet

```python
with open("f.txt", "w") as f:   # write (overwrite/create)
    f.write("text\n")

with open("f.txt", "a") as f:   # append
    f.write("more\n")

with open("f.txt") as f:        # read (default mode "r")
    all_text = f.read()         # whole file as one string
    # or:
    for line in f:              # one line at a time
        print(line.strip())

import os
os.remove("f.txt")              # delete a file
```

---

## Exercises

Run a file with `python exercises/<file>.py`, then compare with the matching
file in [`solutions/`](solutions/). Each solution creates its file, uses it, then
deletes it.

1. [`exercises/01_save_note.py`](exercises/01_save_note.py) — write a note to a file and read it back.
2. [`exercises/02_count_lines.py`](exercises/02_count_lines.py) — write several lines, then count them.
3. [`exercises/03_append_entries.py`](exercises/03_append_entries.py) — write then append, and read the result.

> Try each yourself **before** opening the solution.

---

Next → **19 · Debugging** _(coming soon)_
