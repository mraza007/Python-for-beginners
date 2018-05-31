# Its a simple rock paper scissor game that uses the random module to play instead of a human
from random import *
x = randint(1,3)
if x == 1:
	computer = 'rock'
elif x == 2:
	computer = 'scissor'
else:
	computer = 'paper'
player_1 = input('What is your pick ')
if player_1 == computer:
	print('Its a tie')
elif player_1 == 'scissor':
	if computer == 'rock':
		print('Computer won')
elif player_1 == 'rock':
	if computer == 'scissor':
		print('You won')
elif player_1 == 'scissor':
	if computer == 'paper':
		print('You won')
elif player_1 == 'paper':
	if computer == 'scissor':
		print('Computer Won')
elif player_1 == 'paper':
	if computer == 'rock':
		print('You Won')
elif player_1 == 'rock':
	if computer == 'paper':
		print('Computer Won')



