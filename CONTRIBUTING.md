# Contributing

Thanks for helping make this a better resource for people learning Python! 🐍

This course is aimed at **absolute beginners**, so the guiding principle is:
**clear and simple beats clever.**

## Ways to help
- Fix typos or confusing wording.
- Improve an explanation or add a helpful example.
- Add a new exercise (with a solution).
- Suggest a new lesson or capstone project.

## Lesson structure
Each module under `course/NN-topic/` follows the same shape — please match it:

```
course/NN-topic/
  README.md     the lesson
  examples/     numbered, runnable scripts (01_*.py, 02_*.py, …)
  exercises/    starter files: task in a docstring + a TODO
  solutions/    one solution per exercise, same filename
```

The lesson `README.md` follows this order: a one-line intro → **What you'll
learn** → numbered concept sections (each with a `▶️ Run it` pointer) → a 💡
**Try it yourself** → a **Common mistakes** table → a **Recap / cheat-sheet** →
**Exercises** → a `Next →` link.

## Style guidelines
- Target **Python 3.10+**. Use **f-strings**.
- Keep examples small and focused on the topic at hand.
- Don't use a concept before the lesson that introduces it (e.g. no list
  comprehensions before lesson 12).
- Every `.py` file should run with `python <file>.py` without errors.
- Exercise files state the **exact expected output**; the solution must produce
  it exactly.
- Avoid jargon, or explain it the first time you use it.

## Before you open a pull request
Run every Python file you added or changed and confirm it works:

```bash
# example: check one module
for f in course/07-loops/examples/*.py course/07-loops/solutions/*.py; do
  echo "== $f =="; python3 "$f"
done
```

For interactive files (those using `input()`), test by piping input:

```bash
printf '4\n6\n' | python3 course/08-input-output/solutions/02_add_two_numbers.py
```

Then open a pull request describing what you changed and why. Thank you! 🙌
