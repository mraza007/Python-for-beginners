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
