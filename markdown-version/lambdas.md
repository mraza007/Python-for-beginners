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
* all() takes the iterables and return of they are true or not
```python
list = [1,2,3,4]
all(list)
#This will return true since all the values are true
# You can also check if all numbers are divisible by two in list
```

Lets say you want to check if every name started in the list with the character C

```python
list = ['Casey','Charlie','Courtney','Cashmere']
x = [name[0] == 'C' for name in list]
print(all(x))
#This will return True since every name starts with C
```

Generator Expressions
- They are less memory consuming.
- Readmore on [List vs Generators](https://stackoverflow.com/questions/47789/generator-expressions-vs-list-comprehension)
- 
```python
#A small test \
import sys
list_comp = sys.getsizeof([x for x in range(10)])
gen = sys.getsizeof((x for x in range(10)))
print(f'The mem usage of a list {list_comp} and mem usage of gen {gen}')
```

### Sorted
- This is built in python function that can be used to sort elements in the list or tuple.

```python
x = [7,4,5,2,12]
y = sorted(x,reverse=True)
```
This will sort the list.

Another Example let say we have a dictionary of users and want to sort them.

```python
data = [
{
#
'name':'John',
'class':7,
},
{
'name':'Zayn',
'class':2,
},
{
'name':'Aquaman',
'class':11,
},
{
'name':'Tony',
'class':12,
},
{
'name':'Harry',
'class':5
}
  
]

sorted_dict = sorted(data,key=lambda user:user['class'])

print(sorted_dict) 
```

### Min and Max Function

- This is simple function that returns min or max in the list or tuple.

```python
a = min([1,2,3,4,5])
print(a)
# This returns 1
# if we do max
b = max([1,2,3,4,5])
print(b)
```

### Reverse
- This function reverses list,string or a iterator

```python
x = [1,2,3,4,5]
x.reverse()
# This will reverse a list

for char in reversed("Hello"):
  print(char)
# This will print out reversed hello
```


### Extras
- `abs()` this will return the absolute value.
- `sum()` this will sum a iterable like a list or tuple.
- `round()` This is going to round the number.

```python
x = -10
abs(x) # this is going to print 10
d = [1,2,3,4,5]
sum(d) # This will print the sum of the list.
f = 10.5
round(f) #This will print 11
```

### Zip() 

- Make an iterator that aggregates elements from each of the iterables.
- Returns an iterator of tuples, where the i-th tuple contains the i-th elements from each of the arguement sequences or iterables.
- the iterator stops when the shortest input iterable is exhausted.

```python
x = [1,2,3]
y= [4,5,6]
zip(x,y)
# This will print(1,4),(2,5),(3,6)
# We can also convert it to a dictionary 
dict(zip(x,y))
```
