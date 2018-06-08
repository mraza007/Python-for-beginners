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
