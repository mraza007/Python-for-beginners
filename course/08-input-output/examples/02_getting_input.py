"""input() reads a line of text from the user.

Run me (then type your name and press Enter):
    python 02_getting_input.py
Or feed the answer automatically:
    printf 'Ada\n' | python 02_getting_input.py
"""

name = input("What is your name? ")
print(f"Hello, {name}!")
print("Your name has", len(name), "letters.")
