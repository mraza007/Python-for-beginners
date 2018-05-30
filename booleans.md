#### Booleans and Conditionals
```Python3
# A psuedo code example
if some condition is true:
    do this
elif Some other condition is true:
    Do this
else:
    do something else

```

```Python3
# A real example of Conditonals
if x == 5:
    print('Five')
elif x == 6:
    print('Six')
else:
    print('Nothing is valid')
```

#### Falsiness and Truthiness
* This really matter
* Empty strings, None , 0 has a false value
* Everything else has true value 
```Python
x = input('Whats your favorite TV Show')
if x:
    print('Wow I like that too !')
else:
    print('You have entered nothing') 
# This is an example of the truthiness and falsiness 
# if user enters nothing it will print out nothing
```

#### Comparison Operators

| Op | What it does | Example |
| ------------- | ------------- | ------------- |
| == | Truthy if a has the same value as b | a == b  # True
| != | Truthy if a does NOT have the same value as b | a != b  # False
| > | Truthy if a is greater than b | a > b  # False
| < | Truthy if a is less than be b | a < b  # False
| >= | Truthy if a is greater than or equal to b | a >= b  # True
| <= | Truthy if a is less than or equal to b | a <= b  # True

#### Logical Operators
| Operator | What it does |
| ------------- | ------------- |
| And | Both values have to be true in order to be true |
| Or | If one of the value is true then the entire thing is true |
| Not | Its is like negation |

```Python3
state = input('Enter the state where you live')
if state == 'NJ' or state == 'NY':
    print('You live close to East Coast')
else:
    print('You live far away from the coast')
# In this one of them has to be true
```

```Python3
#Not operator Example
age = 10
not age < 5
# This will be true
```

**Indentation really matters in Python Language and (:) These colons help us indent the blocks**
**You can have multiple (elifs)**