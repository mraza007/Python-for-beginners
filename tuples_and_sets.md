# Tuples and Sets
* Tuples are different from lists they use parenthesis
* They are immmutable and they can't be change or you can't delete a value from it.

```Python
x = (1,2,3,4,5)
#Its a tuple
```

### Why use a Tuple
* They are faster than a list.
* They are safer less bugs and problems
* You can also use tuples as the keys in dictionary

### Different Methods on Tuples
* .count() to see the repetitive element in the list
* .index()

# Sets in Python
* There is no order and they don't have duplicate values
* You can't use index to access the items because there is no order

```Python
set = {1,2,3,4}
# This is how a set looks like
a = set{(1,2,3)}
```


### Set Methods
* .add() it is used to add something to a set
* .remove() it is used to remove something from the set
* .discard() It is also used remove the element from the set
* .clear() it removes everything from the set

### Mathematical Methods in Sets
* | This symbol represents union
* & This represents intersection

```Python
a = {1,2,3,4}
b = {2,3,5}
a | b #This will print {1,2,3,4,5}
a & b # This will print {2,3}
```


### Set Comprehension
* basically its like every other comprehension we have seen
```Python
x = {1,2,3,4}
b = {num+2 for num in x}
```
