#### Python Data Types

* Bool: True or False values
* int : It's an integer like 5,3,4
* str : It's a sequence of characters for example "Your name" this is a string
* list : It's an ordered sequence of different data types for example ['1','apple','10.5']
* tuple : It's an immutable ordered sequence of different data types: ('1', 'apple', '10.5')
* dict : It's a collection of key value pairs {'name':'john'}
* set : It's a collection of unique data: {1, 'apple', 10.5}
* frozenset : It's an immutable collection of unique data: frozenset({1, 'apple', 10.5})
```Python 
x = true # Boolean
y = "Hello World" # This is a string
numbers = [1, 2, 3, 'four'] # this is a list
letters = ('a', 'b', 'c', 'd') # this is a tuple
v = {
    'name':'john',
    'address':'xyz street'
} # Its a dictionary in python

my_set = {1, 'apple', 10.5} # this is a set
my_set.add('banana') # this adds 'banana' to my set : my_set = {1, 'apple', 10.5, 'banana'}
my_set.add('apple') # this won't add nothing because apple is already in the set
my_set.remove('apple') # this removes 'apple' from the set: my_set = {1, 10.5, 'banana'}

my_frozen_set = frozenset(my_set) # this freezes my_set
```

##### Important Note
* Python is dynamically typed language it means that variable can be changed readily but its different in languages like JAVA, C++ C or etc where we have to specify the variable type thats why they are called statically typed languages
* **None Key Word in Python is just like Null**
* **We can use type() Function to see the data type**
