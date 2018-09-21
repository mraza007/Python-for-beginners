# Functions in Python

### What is a Function
* It's process of executing a task
* It can accept an input and return an output

### Why Use Functions
* Stay DontRepeatYourself **DRY** 
* Clean Code no duplication
* for example print() function
* They can help you refactor
* They help us organize things better

#### Syntax
* snakecase
```Python
def function():
    #Here goes everything(block of code)
def say_hi():
    print('Hi')
    #This function will say hi
say_hi() #invoke the function
```

#### Return values from functions
* It exits the function
* Outputs whatever is placed after a return
* Everytime there is a function call there is an instruction added to the stack
```Python
def square_of_two():
    return 2**2

```

#### Parameters in the Functions

```Python
def square(num):
    return num**2
# These parameters only exists in the functions
def add(a,b):
    return a+b    
#Parameters should be named in a better way that makes sense
```

#### Parameters VS Arguements
* Parameter is in the declaration of the function
* Arguement is what we pass into the function

```Python
def multiply(a,b):
    return a * b
print(multiply(1,5))
# a & b are parameters
# 1 & 5 are arguements
# Order matters
```

### Common Mistakes Made while returning in a Function
```Python3
def sum_odd_num(numbers):
    total = 0
    for x in numbers:
        if x%2 ==1:
        `   total +=x
        return total

print(sum_odd_numbers([1,3,5]))        
```
* This function will not return the desired output instead it will return 1 because the return keyword is not indented correctly.
```Python
def sum_odd_num(numbers):
    total = 0
    for x in numbers:
        if x%2 ==1:
        total +=x
    return total

print(sum_odd_numbers([1,3,5]))  
```

* Now the function will return the sum of the odd numbers because we have idented the return keyword

#### Default Parameters
* We can also set the default values in the functions

```Python
def square(num,power=2):
    return num **power
#Even if we dont pass a value for the power it will retain its default value 2
```

* Default parameters can help you save from errors
* It makes our code more flexible
* Default Parameters can be any values we can also pass functions inside of a function

### Passing Functions inside of function
```Python
def add(a,b):
    return a+b
#The math function takes in add function as a parameter also
def math(a,b,fn=add):
    return add(a,b)
```

#### Keyword Arguements
* Using keyword arguements we can alter the order
* The reason we use the keyword arguements is because it helps you cause less errors and makes it more explicit
```Python
def exponent(num,pow):
    return num **pow;
print(exponent(pow=2,num=3)) #This will return 9 
```

#### Scopes
* There are rules where are variables can be accessed
* Whenever we define a variable inside of a function it will be part of the function

```Python
x = 2
def add_two(num):
    return x+num
#In this example the x variable is available outside the function

def add_three(num):
    y = 3
    return num+y
#In this example the y is just the part of the function and it cannot be accessed from outside    
```

* Global scope
* A variable that is defined outside of the function it is global
* If we want to manipulate a variable that is not defined inside of the local scope we use the keyword **global**.

```Python
total = 0
def increment():
    global total
    total +=1
    return total
print(increment())
```

* **non local** keyword 

## Documenting Functions Better
```Python
"""
This will allow us to document the function better
# These are called the docstrings in python
__doc__ they are used to document the functions and it helps us learn better.

print.__doc__
# All built in functions have a docstring

def add(x,y):
    """Add function will take two parameters x and y. Then adds them"""
    return x + y
print(add.__doc__)
"""
```

## ** and * Operators in the Functions

*   * star operator allow us to pass in as much parameters we can and it gathers them as a tuple 
*   The standard keyword is **args but you call it whatever you like.

```Python3
# Lets say we want to add 5 numbers we will write a function and pass 5 parameters
def add(num1,num2,num3,num4,num5):
    return num1+num2+num3+num4+num5
print(add(1,2,3,4,5))

#But what if we want to add 3 number with the same function then we have pass default values and it gets messy and takes a long time so therefore we use *args for function.

def addition(*args):
    total = 0
    for num in args:
        total+=num
    return total
#This is better function now
#args parameter will say the input in the tuple
```

```Python3
# **kwargs parameter this will save the arguements passed into a dictionary 
# **kwargs is standard keyword used in the community
def color(**kwargs):
    for person,color in kwargs.item():
        print(f"{person}'s favorite color is {color}")

```


## Parameter Odering

1) Parameters
2) **args
3) Default Parameters
4) **kwargs

```Python
def odering(a,b,**args,name='john',**kwargs):
    return [a,b,**args,name='john',**kwargs]
```

## List Unpacking

* Passing *values* to unpack the tuples and pass them as arguements in the function

```python3
def addition(*args):
    total = 0
    for num in args:
        total+=num
    return total
x = [1,2,3,4]
# Now we will pass the list inside of the function

print(addition(*x))
```
