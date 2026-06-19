"""while loops repeat as long as a condition is True.

Run me:  python 03_while_loop.py
"""

count = 1
while count <= 3:
    print(count)       # 1, 2, 3
    count += 1         # IMPORTANT: move toward stopping, or it loops forever

print("Done!")

# A while loop is handy when you don't know the number of repeats in advance.
energy = 10
while energy > 0:
    print(f"Energy: {energy}")
    energy -= 4        # subtract until energy runs out
