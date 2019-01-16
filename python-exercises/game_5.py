from __future__ import print_function
import random

try:
    input = raw_input  # Python 2
except NameError:
    pass               # Python 3

min = 1
max = 6

roll_again = "yes"

while roll_again in ("yes", "y"):
    print("Rolling the dices...")
    print("The values are....")
    print(random.randint(min, max))
    print(random.randint(min, max))

    roll_again = input("Roll the dices again?").strip().lower()