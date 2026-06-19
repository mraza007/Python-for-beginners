"""None — the "nothing yet" value.

Run me:  python 04_none_value.py
"""

# None means "no value". It is NOT the same as 0 or "" (empty string).
winner = None
print(winner)         # None
print(type(winner))   # <class 'NoneType'>

# A common use: start a variable as None, fill it in later.
answer = None
answer = 42
print(answer)         # 42

# None is not zero and not an empty string:
print(None == 0)      # False
print(None == "")     # False
