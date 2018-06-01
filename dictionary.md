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