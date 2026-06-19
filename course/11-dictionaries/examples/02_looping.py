"""Looping over keys, values, and items.

Run me:  python 02_looping.py
"""

scores = {"math": 90, "art": 75}

print("Keys:")
for subject in scores:          # looping a dict gives you the KEYS
    print(subject)

print("Values:")
for score in scores.values():
    print(score)

print("Both:")
for subject, score in scores.items():   # key and value together
    print(f"{subject}: {score}")
