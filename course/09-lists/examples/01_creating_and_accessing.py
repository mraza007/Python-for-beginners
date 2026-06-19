"""Creating lists and reading items.

Run me:  python 01_creating_and_accessing.py
"""

fruits = ["apple", "banana", "cherry"]

print(fruits)               # ['apple', 'banana', 'cherry']
print(len(fruits))          # 3   how many items
print(fruits[0])            # apple    (first item — index starts at 0)
print(fruits[-1])           # cherry   (last item)

print("banana" in fruits)   # True
print("mango" in fruits)    # False
