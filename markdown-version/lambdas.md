# Lambdas Functions in Python
Lambdas are one line functions. They are also known as anonymous functions in some other languages. You might want to use lambdas when you don’t want to use a function twice in a program. They are just like normal functions and even behave like them.

```python3
def square(x):
    return x * x
# But Lamdas are totally different

square = lambda x:x*x
print(square(2))
# You can also store lamda inside of a variable
# In this case we are passing x as an parameter. Basically they are short and # anonymous functions
# Lambdas don't have a name'
```

#### Map() function in Lambdas
* It's a standard function that accepts at least two arguements a function and an iterable
* Iterable can be lists tuples or dictionary
* Runs lambda for each value and then returns
```python3
nums = [1,2,3,4,5]
x = map(lambda x:x*x,nums)
print(list(x))
# This shows how map() function works. We are passing lamda function that will square each number in the list nums
```

#### filter() Function
* It takes a list/tuple and filters based on the given condition
* The lambda function needs to be a boolean it can be either true or false
```python3
x = [1,2,3,4,5,6,7,8]
names = ['alex','john','aneesa','aidan','amina','jill','jackson']
data = [
  {'username' : 'alex_1'},
  {'username' : 'axis_07'},
  {'username' : 'aaa'},
  {'username' : 'asthetic'},
  {'username' : 'bob'},
  {'username' : 'jason_07'},
  {'username' : 'razer_07'},
  {'username' : 'pythonista'}
]
# A function that will print the usernames with more than 4 characters
usernames = list(filter(lambda u:len(u['username']) > 4 , data))
for name in usernames:
  print(name['username'])

# A new list with the multiples of two and less than 10
print('\n')
new_list = list(map(lambda num: num*2, filter(lambda num: num < 6   ,x)))
print(new_list)
print('\n')
for nums in new_list:
  print(nums)

# filter names starting with J and adding them to group 1 and names starting with a goes to group_2

group_1 = filter(lambda n:n[0]=='j',names)
print(list(group_1))

group_2 = filter(lambda n:n[0]=='a',names)
print(list(group_2))

# We can also use the list comprehension but it's better to understand how the map() and filter() works
```

#### Any() and all() built in function