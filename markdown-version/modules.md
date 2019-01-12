# Modules
Python modules allows us to reuse our own code or sometimes use somebody else's code.
We can write our own modules or we can use modules written by someone else like `requests`,`datetime` and `etc`.

**Note**: It's just a `python` file.

## Built-in Modules
There built-in python modules that come by default.
List can be found here [LIST OF MODULES](https://docs.python.org/3/py-modindex.html)

- We can import modules by using `import` keyword
- We can also give modules an `alias` when we have long module names like `import random as r`.
- We can also import few functions from the modules `from random import randint`.
- If you want to import everything from random we do something like this `from random import *`

## Custom Modules
Custom module is just file with python code.

##### For Example

```python
# file1.py
def hello():
    return "Hello"
def hey(name):
    return f'Hey {name}'
```

```python
# Importing a custom module
import file1 as fn
fn.hello()
fn.hey('Jake')
```

## External Modules
External modules can be found here [PyPi](https://pypi.org/)
- We can install modules using `pip`, `pip install <package-name>`.
- Pip comes default in `Python 3.4` we can run using `python3 -m pip install <package-name>`.
- `print(dir(<package_name>))` This tells us about the attributes.
- `print(help(package_name))` This tells us everything about the package

## Using PEP8 to cleanup Code

- We can use `autopep8` to fix whitespaces and ident our code
- We can use `autopep8 --in-place <file_name>`


## The `__name__` variable
- The `__name__` variable usually refers to the file name if its the file then it will interpreted as `__main__` 
- If it's a module then `__name__` will be interpreted as the `__file_name__`.

**Note** : use `if __name__ = '__main__' `
