# 🐍 Python for Beginners

A free, hands-on course that takes you from zero to confident with Python —
**no prior experience needed**. Every lesson is short and practical, with
runnable examples and exercises (and solutions) so you learn by *doing*.

> **Two ways to learn:**
> - **▶ Interactive (in your browser):** run and edit every example live — no
>   install. See [Run the interactive course](#run-the-interactive-course).
> - **📖 Plain files:** read the Markdown lessons and run the `.py` files in any
>   editor. Great on GitHub or offline.

---

## Get started

1. **New to Python?** Read **[SETUP.md](SETUP.md)** to install Python (or run the
   browser version) and write your first program.
2. **Ready to learn?** Start with **[01 · Variables](course/01-variables/)** and
   work straight down the list below.
3. **Done with the basics?** Build the **[capstone projects](projects/)**.

Each lesson folder contains:

```
course/NN-topic/
  README.md     ← the lesson (start here)
  examples/     ← runnable example scripts
  exercises/    ← practice files with TODOs
  solutions/    ← worked answers (peek after you try!)
```

---

## Curriculum

### Part 1 — Fundamentals
1. [Variables](course/01-variables/)
2. [Data Types & Numbers](course/02-data-types/)
3. [Strings](course/03-strings/)
4. [Booleans & Comparison](course/04-booleans/)
5. [Operators, Expressions & Statements](course/05-operators/)
6. [Conditionals](course/06-conditionals/)
7. [Loops](course/07-loops/)
8. [Input & Output](course/08-input-output/)

### Part 2 — Data Structures
9. [Lists](course/09-lists/)
10. [Tuples & Sets](course/10-tuples-and-sets/)
11. [Dictionaries](course/11-dictionaries/)
12. [Comprehensions](course/12-comprehensions/)

### Part 3 — Functions & Modules
13. [Functions](course/13-functions/)
14. [Lambdas & map/filter](course/14-lambdas/)
15. [Modules & the Standard Library](course/15-modules/)
16. [Iterators & Generators](course/16-iterators-generators/)

### Part 4 — Real-World Python
17. [Exceptions & Error Handling](course/17-exceptions/)
18. [File Handling](course/18-file-handling/)
19. [Debugging](course/19-debugging/)

### Part 5 — Object-Oriented Programming
20. [Classes & Objects](course/20-classes-and-objects/)
21. [Encapsulation](course/21-encapsulation/)
22. [Static & Class Members](course/22-static-class-members/)

### 🧩 Capstone Projects
- [Number Guessing Game](projects/01-number-guessing-game/)
- [Mad Libs Story](projects/02-mad-libs/)
- [To-Do List](projects/03-todo-list/)

---

## Run the interactive course

The `web/` folder is a small site that renders the lessons and runs Python right
in your browser via [Pyodide](https://pyodide.org) — your code never leaves your
machine.

```bash
# from the project root
python3 -m http.server 8000
```

Then open **<http://localhost:8000/web/>**. Read a lesson, edit any example, and
hit **▶ Run**. (A local server is needed so the page can load the lesson files; a
modern browser is the only other requirement.)

---

## How to use the exercises

1. Open an exercise file — the task and the expected output are in the comment at
   the top.
2. Write your code where it says `# TODO`.
3. Run it: `python course/<module>/exercises/<file>.py`.
4. Compare with the matching file in `solutions/`.

Get stuck and experiment — that's where the learning happens.

---

## Contributing

Found a typo or have an idea for a clearer example or new exercise? Contributions
are very welcome — see **[CONTRIBUTING.md](CONTRIBUTING.md)**.

## License

Released under the [MIT License](LICENSE.md) — free to use, share, and adapt.
