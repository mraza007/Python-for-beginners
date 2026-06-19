# Project 3 · To-Do List

> Skills: lists, loops, functions, conditionals, `input`

A little command-line to-do app. The user types commands to add tasks, list
them, or quit. Tasks live in a list for the duration of the program.

## What to build
1. Keep tasks in a list.
2. Loop, reading a command each time: `add`, `list`, or `done`.
   - `add` → ask for the task text and append it.
   - `list` → print every task, numbered (or "No tasks yet.").
   - `done` → say goodbye and `break`.
3. Anything else → "Unknown command."

## Starter

```python
tasks = []

# TODO:
#  - loop, reading a command with input("Command (add/list/done): ")
#  - handle "add", "list", and "done"
#  - print "Unknown command." for anything else
```

## Run it

```bash
python starter.py
python solution.py
```

A sample session:

```
Command (add/list/done): add
Task: Buy milk
Added: Buy milk
Command (add/list/done): list
1. Buy milk
Command (add/list/done): done
Bye!
```

## Stretch goals
- Add a `remove` command that deletes a task by its number.
- Save the tasks to a file so they survive between runs (see lesson 18).
