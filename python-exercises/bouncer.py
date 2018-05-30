# A Simple Bouncer Program
age = input('What is your age ')
x = int(age)
if x < 18:
	print('Sorry You are too young')
elif x >= 18 and x <= 21:
	print('You are allowed to go')
else:
	print('You are old enough for this')
