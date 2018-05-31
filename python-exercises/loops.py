# A simple example about for loops in python
for x in range(1,21):
	if x == 4:
		print('{} is unlucky').format(x)
	elif x == 13:
		print('{} is unlucky').format(x)
	elif x % 2 == 0:
		print('{} is an even number').format(x)
	elif x%2 != 0:
		print('{} is an odd number').format(x)
	else:
		print(x)