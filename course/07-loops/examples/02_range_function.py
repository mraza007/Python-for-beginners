"""range() generates sequences of numbers.

Run me:  python 02_range_function.py
"""

# range(stop): starts at 0, stops BEFORE stop -> 0,1,2,3,4
print("range(5):")
for n in range(5):
    print(n)

# range(start, stop): 1,2,3,4,5
print("range(1, 6):")
for n in range(1, 6):
    print(n)

# range(start, stop, step): 0,2,4,6,8
print("range(0, 10, 2):")
for n in range(0, 10, 2):
    print(n)
