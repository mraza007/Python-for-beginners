# Python for Beginners — Course Design

_Date: 2026-06-18_

## Goal
Turn the existing notes repo into an easy-to-follow, downloadable course that
anyone can learn Python from, with consistent lessons, runnable examples, and
hands-on exercises (with solutions).

## Decisions
- **Scope:** Full course restructure (numbered, sequential curriculum).
- **Exercises:** Plain `.py` exercise files with instructions in a docstring +
  TODO markers, and a matching solution file. No extra tooling required.
- **Delivery:** Plain repo — Markdown + Python in a clean folder tree. Readable
  on GitHub or locally. Zero build step.
- **OOP:** Consolidate the 25 loose `docs/OOPS/*.py` files into a few coherent
  lessons with curated examples.

## Repository layout
```
README.md                 # Course landing page + full learning path
SETUP.md                  # Install Python + run your first program
course/
  01-variables/
    README.md             # the lesson
    examples/             # numbered, runnable scripts
    exercises/            # starter scripts (task in docstring + TODO)
    solutions/            # matching solution per exercise
  02-data-types/
  ...                     # one folder per module, same shape every time
projects/                 # capstone mini-projects
CONTRIBUTING.md
LICENSE.md
```

## Curriculum
**Part 1 — Fundamentals:** Variables · Data Types & Numbers · Strings ·
Booleans & Comparison · Operators/Expressions · Conditionals (NEW) · Loops ·
Input & Output (NEW)

**Part 2 — Data Structures:** Lists · Tuples & Sets · Dictionaries ·
Comprehensions (NEW)

**Part 3 — Functions & Modules:** Functions · Lambdas & map/filter ·
Modules & Standard Library · Iterators & Generators

**Part 4 — Real-World Python:** Exceptions & Error Handling (NEW) ·
File Handling (NEW) · Debugging

**Part 5 — OOP:** Classes & Objects · Encapsulation · Static/Class members

**Capstone:** 2–3 projects in `projects/` combining skills.

## Lesson README format (every module)
1. Title + "What you'll learn"
2. Concept explanation with small examples
3. "Try it yourself" callouts
4. Common mistakes / gotchas
5. Recap / cheat-sheet
6. Exercises (point to `exercises/`, mention `solutions/`)
7. "Next →" link to the following module

## Conventions
- Python 3.10+; f-strings; light type hints where they aid clarity.
- Every example/exercise/solution runs standalone with `python <file>.py`.
- Fix typos and broken links from the original notes.

## Cleanups bundled in
- Collapse the duplicate `docs/` and `markdown-version/` trees into `course/`.
- Remove the leftover Sphinx config (`docs/source/conf.py`) — no build step.
- Rewrite the top-level README as a real course landing page.

## Build order
1. Build `course/01-variables/` as the reference template (this commit).
2. Review, then roll the format out to all remaining modules.
