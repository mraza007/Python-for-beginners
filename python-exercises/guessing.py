# #This is a simple guessing game in Python.
from random import *
number = randint(1,10)
while True:
	guess = input('Pick a number from 1 to 10: ')
	guess = int(guess)
	if guess < number:
		print('Its too low')
	elif guess > number:
		print('its to high')
	else:
		print('You Won')
		break