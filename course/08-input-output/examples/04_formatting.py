"""Formatting numbers and text inside f-strings.

Run me:  python 04_formatting.py
"""

price = 3.14159
print(f"{price:.2f}")    # 3.14   two decimal places
print(f"{price:.0f}")    # 3      no decimals (rounds)

ratio = 0.25
print(f"{ratio:.0%}")    # 25%    shown as a percentage

name = "Sam"
print(f"|{name:<8}|")    # |Sam     |   left-aligned within 8 characters
print(f"|{name:>8}|")    # |     Sam|   right-aligned within 8 characters
