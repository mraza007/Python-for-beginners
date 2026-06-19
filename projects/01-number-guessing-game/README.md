# Project 1 · Number Guessing Game

> Skills: `random`, `while` loops, conditionals, `input` and `int()`

The computer picks a secret number between 1 and 10. The player keeps guessing
until they get it, with a "Too high!" / "Too low!" hint after each guess.

## What to build
1. Pick a secret number with `random.randint(1, 10)`.
2. Loop, reading a guess each time with `int(input(...))`.
3. Print `"Too low!"` if the guess is below the number, `"Too high!"` if above.
4. When the guess is correct, print a win message and `break`.

## Starter

```python
import random

number = random.randint(1, 10)
print("I'm thinking of a number between 1 and 10.")

# TODO:
#  - loop until the guess is correct
#  - read a guess with int(input("Your guess: "))
#  - print "Too low!" / "Too high!" hints
#  - on a correct guess, print a win message and break
```

## Run it

```bash
python starter.py     # your version
python solution.py    # the reference version
```

## Stretch goals
- Count how many guesses it took and report it at the end.
- Let the range be 1–100.
- Handle non-number input gracefully with `try` / `except` (see lesson 17).
