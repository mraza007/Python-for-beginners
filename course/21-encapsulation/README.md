# 21 · Encapsulation

> **Part 5 — Object-Oriented Programming** · Estimated time: 25–35 min · Prerequisite: 20 · Classes & Objects

**Encapsulation** means bundling data with the methods that control it, and
*hiding* the internal data so it can only change in safe, valid ways. Instead of
letting anyone poke at an object's insides, you expose a tidy set of methods. The
classic example: a bank balance should only change through `deposit` and
`withdraw`, never by someone setting it to `-9999` directly.

## What you'll learn
- Why fully-public data is risky
- Marking attributes "private" with a leading `__`
- Controlling changes with methods (validation)
- Reading values safely with **getter** methods

---

## 1. The problem with public data

```python
class Account:
    def __init__(self):
        self.balance = 0

acc = Account()
acc.balance = -9999     # nothing stops this nonsense
print(acc.balance)      # -9999  — an invalid balance!
```

Anyone can set a public attribute to anything. For important data, that's a bug
waiting to happen.

▶️ **Run it:** `python examples/01_public_problem.py`

---

## 2. Private attributes with `__`

Prefix an attribute with **two underscores** to make it private — usable inside
the class, hidden from outside. Now changes must go through your methods, where
you can **validate** them.

```python
class Account:
    def __init__(self):
        self.__balance = 0          # private

    def deposit(self, amount):
        if amount > 0:              # we decide what's allowed
            self.__balance += amount

    def show(self):
        print("Balance:", self.__balance)

acc = Account()
acc.deposit(100)
acc.show()                # Balance: 100

try:
    print(acc.__balance)  # blocked from outside
except AttributeError as e:
    print("Can't access it directly:", e)
```

▶️ **Run it:** `python examples/02_private_attribute.py`

> 💡 **Try it yourself:** add a `deposit` call with a negative amount and confirm
> the balance doesn't change.

---

## 3. Getters: safe read access

A **getter** method lets the outside *read* a private value without being able to
overwrite it. Combined with validating methods, you fully control the data.

```python
class Account:
    def __init__(self):
        self.__balance = 0

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:   # can't overdraw
            self.__balance -= amount

    def get_balance(self):                 # read-only access
        return self.__balance

acc = Account()
acc.deposit(100)
acc.withdraw(30)
acc.withdraw(1000)        # ignored — not enough funds
print(acc.get_balance())  # 70
```

▶️ **Run it:** `python examples/03_getter_method.py`

---

## Common mistakes

| Mistake | What happens | Fix |
|---|---|---|
| `acc.__balance` from outside | `AttributeError` | Use a method like `get_balance()`. |
| Expecting `__` to be unbreakable security | it's a strong convention, not a lock | Treat it as "hands off", not encryption. |
| Validating in some methods but not others | bad data sneaks in | Funnel *all* changes through validating methods. |
| Single underscore `_x` | only a *hint* ("internal"), not hidden | Use `__x` for name-mangled privacy. |

---

## Recap / cheat-sheet

```python
class Account:
    def __init__(self):
        self.__balance = 0          # private (leading __)

    def deposit(self, amount):      # change through a validating method
        if amount > 0:
            self.__balance += amount

    def get_balance(self):          # getter: safe read access
        return self.__balance

# acc.__balance   -> AttributeError (hidden)
# acc.get_balance()  -> ok
```

---

## Exercises

Run a file with `python exercises/<file>.py`, then compare with the matching
file in [`solutions/`](solutions/).

1. [`exercises/01_bank_account.py`](exercises/01_bank_account.py) — deposit into a private balance.
2. [`exercises/02_reject_negative.py`](exercises/02_reject_negative.py) — validate deposits.
3. [`exercises/03_counter_private.py`](exercises/03_counter_private.py) — a counter with a hidden count.

> Try each yourself **before** opening the solution.

---

Next → **22 · Static & Class Members** _(coming soon)_
