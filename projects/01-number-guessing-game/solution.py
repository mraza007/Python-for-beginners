"""Project 1 — Number Guessing Game (one solution).

Run with:  python solution.py
"""

import random

number = random.randint(1, 10)
guesses = 0
print("I'm thinking of a number between 1 and 10.")

while True:
    guess = int(input("Your guess: "))
    guesses += 1
    if guess < number:
        print("Too low!")
    elif guess > number:
        print("Too high!")
    else:
        print(f"You got it in {guesses} guesses! 🎉")
        break
