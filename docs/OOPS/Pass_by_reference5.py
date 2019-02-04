'''
For changes to reflect outside the function, the object must be mutable object. 
All objects created through custom classes are mutable objects. 
If the objects are immutable, the changes don't reflect outside the function. 
This is because any changes made to a immutable object creates a new object. 
In the below code you can see that when we try to modify the string, it creates 
a new string object and the original string object is unchanged.
'''

def change(strng):
    print("Object ID before modification ",id(strng))
    strng=strng.upper()
    print("Object ID after modification ",id(strng))

s1="hello"
change(s1)
print(s1)
