"""Reading characters by index, and slicing out pieces.

Run me:  python 03_indexing_and_slicing.py
"""

word = "Python"
#       0123456  -> indexes start at 0
#       P=0 y=1 t=2 h=3 o=4 n=5

print(word[0])    # P   first character
print(word[-1])   # n   last character (negative counts from the end)

# Slicing: word[start:stop] -> from start, up to BUT NOT including stop.
print(word[0:3])  # Pyt
print(word[3:])   # hon  (no stop -> go to the end)
print(word[:2])   # Py   (no start -> begin at 0)
print(word[2:5])  # tho
