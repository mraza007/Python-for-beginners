#Its a simple Rock paper scissor game
print('...Rock...')
print('...Paper...')
print('...Scissor...')
x = input('Enter Player 1 Choice ')
print('No Cheating\n\n' * 20)
y = input('Enter Play 2 Choice ')
if x == 'paper' and y == 'rock':
	print('Player 1 won')
elif x == 'rock' and y == 'paper':
	print('Player 2 wins')
elif x == 'scissor' and y == 'paper':
	print('Player 1 wins')
elif x == 'paper' and y == 'scissor':
	print('Player 2 wins ')
elif x == 'rock' and y == 'scissor':
	print('Player 1 wins')
elif x == 'scissor' and y == 'rock':
	print('Player 2 wins ')
else:
	print('Something else went wrong')