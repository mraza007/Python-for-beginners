### Strings in  Python
* Strings in python can be in either double quotes or single quotes
```Python
my_str = 'Hello World'
string = "Hello"
```

#### String Concatenation
* We Concatenate strings using **+** operator 
```Python
str1 = 'Hello'
str2 = 'World'
print(str1+str2)
#This will print out Hello World
```
* You cannot concatenate strings with integers

```Python
8 + 'hello'
# This will give an error
but we can do this using an str() function and it will convert the the int into str then you can concatenate
```

* You can also use the **+=** operator to concatenate strings

```Python
string = "Cat"
string += " Dogs"
print(string)
#This will print out Cat Dogs
```

#### Formatting Strings
There's a new method to interpolate the strings 
* The method is called the F-strings this will help you convert the int value into a string 
```Python
x = 10
print(f"I have told you " {x}  times to clean the floor correctly")
```
