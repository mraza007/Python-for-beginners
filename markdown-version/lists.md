## Lists in Python 
* Lists is a way of combining different data structures.Its is more like grouping elements together.
* They are usually becuase they make your code more readable.
```Python
x = [1,2,3,4,'five']
#This is how a list looks like
# They can hold different data such as numbers strings and floats
# Values in the lists are seperated by the commas
```

### List built in Functions
* Len() This function tells how many items are there in the list
```Python
x = ['one,'two','three']
print(len(x))
# This will printout the number of items present in the list
```
* list() function converts to list
```Python
x = range(1,4)
print(list(x))
# this print [1,2,3]
```

### Different way of accessing the data in the lists
* Every element in the list starts at 0
* You can also use negative numbers but it will get the data from backwards
```Python
x = ['john','jason','tony']
print(x[0]) # This will john
print(x[1]) # This will jason
print(x[2]) # This will tony
```

* We use built in python **in** keyword to see if the item exists in the list
```Python
x = [1,2,3]
1 in x
# this will print true
4 in x
#this will print false because 4 is not in the list
```

### We can also iterate throught the list using loops
```Python
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

#### These methods are used to add items to the list
* append () this method will add the item to the end of the list.
* extend() this method adds all the values at the end of the list
```Python
x = [1,2,3,4,5]
x.append([5,6,7,8])
# This print [1,2,3,4,5,[5,6,7,8]]
#Lets use the extend method on this
x.extend([5,6,7,8,9])
#This will print out [1,2,3,4,5,5,6,7,8,9]
```
* if want to add one item to the end of the list use append() if you are adding more than one item use extend()
* insert() method is used to add the item to the given position in the list
```Python
x = [1,2,3,4]
x.insert(1,'hi')
[1,'hi',2,3,4]
```

#### Methods that are used to delete items from the list
* clear() method will remove all the items in the list at once
* pop() method removes the element at the given position
```Python
x = [1,2,3,4]
x.pop()# this will remove the last item by default
x.pop(1)
#this will remove the item at index [1]
```
* remove() method this takes in the value
```Python
x = [1,2,3,4]
x.remove(1)
#this will remove 1 in the list
[2,3,4]
```

#### Other List Methods
* index()
* count(), This method is used to count the duplicates in the list
* reverse () this will reverse the list. This doesn't take arguements
* sort() This function will sort the list in ascending order'
* .join () this is string method **Only works if there are strings in the lists**
```Python
x = [1,'hi',2,3,4]
x.index(1)
#this will print the index of the 1 which is 0
x = [1,1,2,3,4,5]
x.count(1)
#This will check if the element is being repeated 
x.reverse()
#This method will reverse the list
# the output is going to be like [4,3,2,'hi',1]
x = [3,2,4,1]
x.sort()
#This will sort out the list
# The output will be [1,2,3,4]
x = ['1','2','3']
' '.join(x)
#Output 1 2 3
#this will add the space
```

### Lists Slicing      
* It is used to make new lists from old lists
```Python
#lists slicing
# some_list[start:end:step]
# start is to where to start
# end is to where to end
# Step is the intervals

x = [1,2,3,4,5,6]
x[0:2]
# This will print [1,2] 3 is not included becuase its exclusive
x[0:7:2]
#This will print [2,4,6]
# Easy way to reverse a list x[::-1]
#Swapping Lists
y = ['John','Jason']
y[0],y[1] = y[1],y[0]
```

### List Comprehension
* List comprehensions are used for creating new list from another iterables.
* Interesting articles on  [List Comprehension](https://hackernoon.com/list-comprehension-in-python-8895a785550b)
```Python
nums = [1,2,3,4,5,6,7,8]
y = [x*x for x in nums]
# This will print 
[1,4,9,16,25]
# We can also use a loop
new_list =[]
for x in nums:
    sqaure = x*x
    new_list.append(square)
#This piece of code is doing the same thing but the only difference is that the other method is much easier
# This can also be used to convert into strings
[str(x) for x in nums]
# This will print everything in the list that was present in int.
# We can also use the conditonal statements in lists
[x for x in num if x%2==0]
#This will print all the even numbers in the lists
```

