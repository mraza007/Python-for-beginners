#Heads & Tail
from random import random

def heads_tails():
	r = random()
	if r > 0.5:
		return "HEADS"
	else:
		return "TAILS"

print(heads_tails())

# This function generates even numbers
def generate_evens():
	even = [x for x in range(1,50) if x % 2==0]
	return even

print(generate_evens())