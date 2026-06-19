"""Input is text — convert it before doing maths.

Run me (then type a whole number):
    python 03_input_numbers.py
Or feed the answer automatically:
    printf '20\n' | python 03_input_numbers.py
"""

age_text = input("How old are you? ")   # e.g. "20" — a string
age = int(age_text)                     # convert to a number
print(f"Next year you'll be {age + 1}.")
