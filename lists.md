## Lists in Python 
* Lists is a way of combining different data structures.Its is more like grouping elements together.
* They are usually becuase they make your code more readable.
```Python3
x = [1,2,3,4,'five']
#This is how a list looks like
# They can hold different data such as numbers strings and floats
# Values in the lists are seperated by the commas
```

### List built in Functions
* Len() This function tells how many items are there in the list
```Python3
x = ['one,'two','three']
print(len(x))
# This will printout the number of items present in the list
```
* list() function converts to list
```Python3
x = range(1,4)
print(list(x))
# this print [1,2,3]
```

### Different way of accessing the data in the lists
* Every element in the list starts at 0
* You can also use negative numbers but it will get the data from backwards
```Python3
x = ['john','jason','tony']
print(x[0]) # This will john
print(x[0]) # This will jason
print(x[0]) # This will tony
print(x[1])
print(x[2])
```

* We use built in python **in** keyword to see if the item exists in the list
```Python3
x = [1,2,3]
1 in x
# this will print true
4 in x
#this will print false because 4 is not in the list
```

### We can also iterate throught the list using loops
```Python3
list = ['blue','yellow','green','orange','black']
for color in list:
    print(list)
# Using while loop
i = 0
while i < len(list):
    print(list[i])
    i += 1 
#len() function tells us how many items are there in the list        
```
**Note: len() can also be used on the strings**
### List Methods
* Built-in python list methods 
* append () this method will add the item to the end of the list.
* extend() this method adds all the values at the end of the list
```Python3
x = [1,2,3,4,5]
x.append([5,6,7,8])
# This print [1,2,3,4,5,[6,7,8,9]]
#Lets use the extend method on this
x.extend([5,6,7,8,9])
#This will print out [1,2,3,4,5,6,7,8,9]
```
* if want to add one item to the end of the list use append() if you are adding more than one item use extend()
* insert() method is used to add the item to the given position in the list
```Python3
x = [1,2,3,4]
x.insert(1,'hi')
[1,'hi',2,3,4]
```
