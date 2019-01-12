# Debugging Python Code
- Try and Else Block
- Pdb
- set trace method

## Common Python Errors
- `SyntaxError`
- `NameError` This usually occurs when a variable is not defined or it hasn't been assigned yet.
- `TypeError` This usually occurs when an operation or function is applied to a wrong type.
- `IndexError` This occurs when we are trying to access an element in a list using invalid index.
- `ValueError`  This occurs when a built in operation or function receives an arguement that has the right type but an inappropiate value
- `KeyError` This occurs when a dictionary doesn't have a specific key.
- `AttributeError` This occurs when a variable doesn't have an attribute. 

## Raising Our own Exceptions
- We can raise our own error exceptions 

```python
raise ValueError('invalid Error')
```

- Lets say we have a simple function and we want it to have our own exception.

```python
def color(text,color):
    if type(text) is not str:
        raise TypeError('Enter a valid String')
    print(f'This {text} is using {color}.')
```

## Handling Errors
- In python we can handle errors using `try` and `except`

```python
try:
    x
except ValueError:
    print("there's a error")
```

`Else` and `Finally`.
`Finally` would run no matter what.

```python
# a small program
try:
    x = int(input("Enter a number"))
except:
    print("Enter a valid Number")
else:
    print("Thanks for a valid number")
finally:
    print("I will run no matter what hehehe")
```

## Debugging our code using `PDB`

- In order to set a breakpoint we use `pdb.set_trace()`
- After setting a breakpoint then we can go line by line through our code.

#### Common `PDB` commands
- `l` List 
- `n` next line
- `p` print
- `c` continue
