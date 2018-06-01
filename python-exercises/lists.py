# A simple shopping list program that uses python lists
shopping_list = []
print('Hi Welcome to Personalized Shopping List ')
user_input = input('What items would you like to add ')
while True:
	shopping_list.append(user_input)
	user_input = input('Would you like to add more or list ')
	if user_input == 'list':
		for item in shopping_list:
			print(item)
		else:
			break