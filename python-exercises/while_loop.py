# A simple while loop example
user_input = input('Hey how are you ') 
while user_input != 'stop copying me':
	print(user_input)
	user_input = input()
else:
	print('UGHH Fine')