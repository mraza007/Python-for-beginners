### Loops in Python
* What loops are in Python
* While loops and For Loops in Python

### For Loops 
* They can be used to iterate the number of elements in the lists,
* They can also be used to iterate the strings
* range function is used to iterate through numbers
```Python3
for item in iterable_object:
    print(item)
# This is the syntax for loops in python
# Item represents the iterator's position
# You can call it anything you want
# printing numbers using for loops
for number in range(1,100):
    print(number)
# This will print numbers from 1 to 99
for letter in "Hello":
    print(letter)
# This for loop will print out the characters in the word hello
```

#### Ranges
* They are usually used with for loops
* range(7) if we give in one parameter this will only print out numbers 0 to 6 
* range(1,8) if we give in two parameters this will print out numbers 1 to 7 
* range(1,10,2) In this example the thir parameter is used to tell how many steps should be skipped and this will print odd numbers 
* range helps you generate the sequence of number its a python built in function

```Python3
x = input('How many times I have told you clean the room ')
y = int(x)
for time in range(y):
    print(f'{time}: Clean Your room')
# A simple example of loops

```

### While Loops
* While loops are just like for loops
* While loops only run if the conditional statement is true otherwise it will stop
```Python3
while some_condition:
    #do this
# An example 
user_input = None
while user_input != 'please':
    print('Sorry Access Denied')
```
* We need to be careful with while loops since they will continue forever if the condition is not true **It will ruin the program**

```Python3
#Another While Loop Example
num = 0
while num < 10:
    num +=1
    print(num)
```


#### Importance of Break keyword in Python
* It gives us the ability to get out of the loop
```Python
while True:
    command = input('Type exit to get out of this')
    if command == 'exit':
        break


for x in range(1,10):
    if x == 3:
        break
```