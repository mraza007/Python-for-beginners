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