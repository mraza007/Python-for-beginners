# 11 · Dictionaries

> **Part 2 — Data Structures** · Estimated time: 30–40 min · Prerequisite: 09 · Lists

A **dictionary** stores data as **key → value** pairs, like a real dictionary
maps a word to its definition. Where a list finds things by *position*, a
dictionary finds them by a meaningful *name* (the key). It's the perfect tool for
"look something up": a contact's phone number, a product's price, a player's
score.

## What you'll learn
- Creating dictionaries and reading values **by key**
- Adding, updating, and the safe `.get()` lookup
- Checking for keys with `in`, and removing with `.pop()`
- Looping over keys, values, and `.items()` (both at once)

---

## 1. Creating and accessing

```python
person = {"name": "Ada", "age": 36}

print(person["name"])    # Ada    look up by key
print(len(person))       # 2      number of pairs

person["age"] = 37       # update an existing key
person["city"] = "London"  # add a new key
print(person)            # {'name': 'Ada', 'age': 37, 'city': 'London'}
```

Looking up a key that doesn't exist with `[]` raises a `KeyError`. Use `.get()`
to ask safely:

```python
print(person.get("email"))         # None  (no crash)
print(person.get("email", "n/a"))  # n/a   (your own default)
```

▶️ **Run it:** `python examples/01_creating_and_accessing.py`

---

## 2. Looping over a dictionary

```python
scores = {"math": 90, "art": 75}

for subject in scores:            # loops over the KEYS by default
    print(subject)

for score in scores.values():     # just the values
    print(score)

for subject, score in scores.items():   # key AND value together
    print(f"{subject}: {score}")
```

`.items()` is the one you'll reach for most — it hands you both pieces at once.

▶️ **Run it:** `python examples/02_looping.py`

> 💡 **Try it yourself:** loop over `scores.items()` and print only the subjects
> where the score is 80 or above.

---

## 3. Checking and removing

```python
inv = {"apples": 5, "pears": 2}
print("apples" in inv)   # True   (in checks the KEYS)
print("milk" in inv)     # False

removed = inv.pop("pears")   # remove a key and get its value back
print(removed)               # 2
print(inv)                   # {'apples': 5}

inv.update({"apples": 10, "bread": 3})   # update existing + add new
print(inv)                   # {'apples': 10, 'bread': 3}
```

▶️ **Run it:** `python examples/03_methods.py`

---

## Common mistakes

| Mistake | What happens | Fix |
|---|---|---|
| `person["email"]` when missing | `KeyError` | Use `person.get("email")` or check `"email" in person`. |
| Expecting `in` to check values | `in` checks **keys** | Use `value in person.values()` for values. |
| Using a list as a key | `TypeError` (unhashable) | Keys must be immutable — use a string, number, or tuple. |
| Two pairs with the same key | the later one wins | Keys are unique; assigning again overwrites. |

---

## Recap / cheat-sheet

```python
d = {"a": 1, "b": 2}
d["a"]                 # 1   look up by key
d["c"] = 3             # add / update
d.get("x", default)    # safe lookup
"a" in d               # key membership
d.pop("a")             # remove key, return value
len(d)                 # number of pairs

for k in d: ...            # keys
for v in d.values(): ...   # values
for k, v in d.items(): ... # both
```

---

## Exercises

Run a file with `python exercises/<file>.py`, then compare with the matching
file in [`solutions/`](solutions/).

1. [`exercises/01_lookup.py`](exercises/01_lookup.py) — look up a value by its key.
2. [`exercises/02_inventory.py`](exercises/02_inventory.py) — add to and update a stock dictionary.
3. [`exercises/03_total_prices.py`](exercises/03_total_prices.py) — total all the values in a dictionary.

> Try each yourself **before** opening the solution.

---

Next → **12 · Comprehensions** _(coming soon)_
