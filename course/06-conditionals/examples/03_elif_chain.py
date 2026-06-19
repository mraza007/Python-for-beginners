"""elif: check several conditions in order; first match wins.

Run me:  python 03_elif_chain.py
"""

score = 85

if score >= 90:
    print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
else:
    print("F")

# 85 >= 80 is reached before 85 >= 70, so the answer is B.
