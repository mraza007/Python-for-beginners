import random
x = random.randint(1, 10)
a = -1
print('Guess the number from 1 to 10')
while a != x:
	a = int(input('>>>'))
	if a == x:
		print('You win')
	elif a < x:
		print('The number is greater')
	else:
		print('The number less than the guess')