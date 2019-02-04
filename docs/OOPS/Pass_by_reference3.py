'''
In python, everything is an object. 
Hence when we pass a list to a function and when we modify the list, 
the changes are reflected outside the function as well. 
For example, we can see that there is only one object and value and data are references to that object.
'''

def change_function(data):
    print ("Id of list received in method", id(data))
    data[1] = 500
    print ("Id of list after element modification in method", id(data))

value = [100, 200, 300]
print ("List and its id before method call", value, id(value))
change_function(value)
print ("List and its id after method call ", value, id(value))
