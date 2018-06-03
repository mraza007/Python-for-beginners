### Dictionaries in Python
* Dictionaries vs List. Lists have its own limitations like it can contain one data type and data can't be modeled correctly if we are using lists
* Dictionary is a data structure that contains key value pairs
* Keys are used to describe the data
* Values are used to represent the data

#### This is how a dictionary looks like
**Note: key-value pairs are separated by the commas **

```Python
info = {
    'name':'John',
    'city':'New York',
    'own_a_car':True,
}
#We can also use the dict() built in python function to generate keys
x = dict(name='John',age='21')
print(x)
#This will print x
{
    'name':'John'
    'age':'24'
}
```

* To access the values in the dictionary we pass in the value

```Python
info = {
    'name':'John',
    'city':'New York',
    'own_a_car':True,
}
info['name'] #This will print John
```

* To iterate values and keys at once we use this function .keys() and .values()
 
```Python
info = {
    'name':'John',
    'city':'New York',
    'own_a_car':True,
}
for x in info.keys(): #This will print keys
  print(x)
print(' ')
for y in info.values(): #This will print valuesq
  print(y)  
```

* To iterate both values and keys together we use .items()
```Python
info = {
    'name':'John',
    'city':'New York',
    'own_a_car':True,
}
for keys,values in info.items():
    print(keys,values)
    #This will print keys and values
```

#### To check if keys and values are present in the dictionary

```Python
info = {
    'name':'John',
    'city':'New York',
    'own_a_car':True,
}
name in info
# This will print true because name is key in info

John in info.values()
#This will also print true because its present in the dictionary
```

### Dictionary Methods
* .clear() method clears the entire dictionary
* .copy() makes the entire copy of the list
* .fromkeys([])

```Python
info = {
    'name':'John',
    'city':'New York',
    'own_a_car':True,
}
info.clear() # This will clear the whole dictionary
a = info.copy()
print(a)
#This will print the entire info dictionary

new_user = {}.fromkeys(['name','email','city'],'False')
# This will create a new dictionary
new_user = {
    'name':'False'
    'email':'False'
    'city':'False'
}
```

* .get() is used to retrieve the value from the dictionary

```Python
info = {
    'name':'John',
    'city':'New York',
    'own_a_car':True,
}
info.get('name')
#This will print John
```

### More Dictionary Methods

* .pop() In this method we have to provide the key
* .popitem()removes a random key in the dictionary
* .update()

### Dictionary Comprehension
* They use the same syntax like the lists we just use the dictionary brackets
* It will iterate over keys by default by we can use the .items() to iterate over values too

```Python
a = dict(a=1,b=2,c=3,d=4)
b = {key:value **2 for key,value in a.items()}
#This will print out the the square of each number in b
# This will allow us to make dictionaries out of a dictionary that's one of the reason we use the dictionary comprehension.
#Another example of dictionary comprehension.
c = {key:value+2 for key,value in a.items()}

```