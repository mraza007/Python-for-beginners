"""break stops the loop; continue skips to the next round.

Run me:  python 04_break_and_continue.py
"""

# break: stop the whole loop early.
for n in range(1, 10):
    if n == 5:
        break          # leave the loop the moment n is 5
    print(n)           # 1, 2, 3, 4

print("---")

# continue: skip the rest of THIS round, move to the next.
for n in range(1, 7):
    if n % 2 == 0:
        continue       # skip even numbers
    print(n)           # 1, 3, 5
