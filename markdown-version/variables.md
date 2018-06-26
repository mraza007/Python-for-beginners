### Variable in Python 
In this section we are going to learn how to represent variables in the Python language. Please note that variables in Python are dynamically typed, which means unlike languages like Java and C++, you don't need to specify whether the variable is a string, integer, etc.

There are some basic conveniences Python variables provide:

* Variables can be reassigned at any time
* We can also assign variables together (more on this later)
* We can also assign variables to each other

```Python
x = 100
y = 10
all, us , about = 10, 11 ,12
# In this case we have assigned variables at once
print(x+y) # This will print 110
print(us) # To see if it is going to print the us variable that we declared
```
#### Variable Naming Conventions

There are some naming variable conventions used in python language: 

* A variable name cannot start with a number. For instance, if you write something like `2morrow = 'day after'`, Python will complain loudly. 
* Variable names are case-sensitive. `total` and `Total` are _not_ the same variable.
* Variables should be snake_case (that is, small caps with words joined by underscores). Please note that this is just a convention in the Python community, as we believe this lends to clearer, easily readable code.
* Camelcase is usually used for class names. For instance, `RssReader`.
* There are some predefined variables in Python that start with dunder (double underscores), for example, `__dir__`. **Don't Touch Them. Ever.**

```Python
2cats = 10 #This is wrong
_cats = 10 #This is totally fine 
hey@hey = 10 # This is not good

cats != CATS
# In this case python language reads them differently

__dont_touch__ #Dunder Variable
``` 
