# 20 · Classes & Objects

> **Part 5 — Object-Oriented Programming** · Estimated time: 35–45 min · Prerequisite: 13 · Functions

**Object-Oriented Programming (OOP)** lets you model real-world things — a dog, a
bank account, a phone — in code. A **class** is a blueprint; an **object** (or
*instance*) is a specific thing built from that blueprint. Classes bundle
**data** (attributes) and **behaviour** (methods) together.

## What you'll learn
- The idea of a class (blueprint) vs an object (instance)
- Defining a class with `__init__`, and what `self` means
- **Attributes** (data) and **methods** (behaviour)
- Creating many independent objects from one class
- Making objects print nicely with `__str__`

---

## 1. Your first class

```python
class Dog:
    def __init__(self, name):    # the constructor — runs when a Dog is created
        self.name = name         # store data on THIS object via self

    def bark(self):              # a method: a function that belongs to the class
        return f"{self.name} says Woof!"

rex = Dog("Rex")        # create (instantiate) an object
fido = Dog("Fido")

print(rex.name)         # Rex
print(rex.bark())       # Rex says Woof!
print(fido.bark())      # Fido says Woof!
```

`self` is how an object refers to itself. You never pass it in by hand — Python
fills it in. Class names use `CamelCase` by convention.

▶️ **Run it:** `python examples/01_first_class.py`

---

## 2. Attributes and methods

**Attributes** describe what an object *is*; **methods** describe what it *does*.

```python
class Mobile:
    def __init__(self, brand, price):
        self.brand = brand        # attributes
        self.price = price

    def purchase(self):           # method
        discount = 10 if self.brand == "Apple" else 5
        final = self.price - self.price * discount / 100
        return f"{self.brand} costs {final} after discount"

phone = Mobile("Apple", 1000)
print(phone.brand)        # Apple
print(phone.purchase())   # Apple costs 900.0 after discount
```

▶️ **Run it:** `python examples/02_attributes_and_methods.py`

> 💡 **Try it yourself:** add a `describe()` method to `Mobile` that returns
> `"Apple phone, $1000"`.

---

## 3. Many independent objects

Each object built from a class has its **own** data. Changing one doesn't affect
the others.

```python
class Counter:
    def __init__(self):
        self.value = 0
    def increment(self):
        self.value += 1

a = Counter()
b = Counter()
a.increment(); a.increment()
b.increment()
print("a:", a.value)   # 2
print("b:", b.value)   # 1  (completely independent)
```

▶️ **Run it:** `python examples/03_multiple_objects.py`

---

## 4. Printing objects with `__str__`

By default, printing an object shows something cryptic like
`<__main__.Book object at 0x...>`. Define `__str__` to control what `print`
shows.

```python
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
    def __str__(self):
        return f"{self.title} by {self.author}"

print(Book("Python 101", "Guido"))   # Python 101 by Guido
```

▶️ **Run it:** `python examples/04_str_method.py`

---

## Common mistakes

| Mistake | What happens | Fix |
|---|---|---|
| Forgetting `self` in a method's parameters | `TypeError` about arguments | Every method's first parameter is `self`. |
| Forgetting `self.` when storing data | the value is lost after `__init__` | Save it as `self.name = name`. |
| Calling a method without `()` | you get the method object, not its result | Call it: `rex.bark()`. |
| Confusing the class with an instance | `Dog.bark()` needs an object | Make one first: `Dog("Rex").bark()`. |

---

## Recap / cheat-sheet

```python
class Thing:
    def __init__(self, x):   # constructor
        self.x = x           # attribute on the instance

    def method(self):        # behaviour; self = this object
        return self.x

    def __str__(self):       # how print() shows it
        return f"Thing({self.x})"

obj = Thing(5)               # create an instance
obj.x                        # read an attribute
obj.method()                 # call a method
```

---

## Exercises

Run a file with `python exercises/<file>.py`, then compare with the matching
file in [`solutions/`](solutions/).

1. [`exercises/01_make_a_dog.py`](exercises/01_make_a_dog.py) — define a class with a method.
2. [`exercises/02_rectangle_class.py`](exercises/02_rectangle_class.py) — store attributes and compute from them.
3. [`exercises/03_book_str.py`](exercises/03_book_str.py) — add a `__str__` method.

> Try each yourself **before** opening the solution.

---

Next → **21 · Encapsulation** _(coming soon)_
