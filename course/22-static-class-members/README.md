# 22 · Static & Class Members

> **Part 5 — Object-Oriented Programming** · Estimated time: 25–35 min · Prerequisite: 20 · Classes & Objects

Some data belongs to *each object* (one name per dog); other data belongs to *the
class as a whole* (every dog is the same species). This lesson covers **class
attributes** shared by all instances, plus `@staticmethod` and `@classmethod` —
methods that don't need a particular object.

## What you'll learn
- **Instance** attributes vs **class** attributes (per-object vs shared)
- Using a class attribute to count instances
- `@staticmethod` — a utility function living on the class
- `@classmethod` — a method that receives the class (`cls`)

---

## 1. Instance vs class attributes

An **instance attribute** (set with `self.`) is unique to each object. A **class
attribute** (defined directly in the class body) is **shared** by every instance.

```python
class Dog:
    species = "Canis familiaris"    # CLASS attribute — shared by all dogs

    def __init__(self, name):
        self.name = name            # INSTANCE attribute — unique per dog

a = Dog("Rex")
b = Dog("Fido")
print(a.name, b.name)         # Rex Fido                          (different)
print(a.species, b.species)   # Canis familiaris Canis familiaris (shared)
```

▶️ **Run it:** `python examples/01_class_vs_instance.py`

---

## 2. Counting instances with a class attribute

Because a class attribute is shared, it's perfect for tracking something across
all objects — like how many have been created.

```python
class Player:
    count = 0                 # shared across every Player

    def __init__(self, name):
        self.name = name
        Player.count += 1     # bump the shared counter

Player("Ann")
Player("Bo")
Player("Cy")
print("Players created:", Player.count)   # 3
```

▶️ **Run it:** `python examples/02_counting_instances.py`

> 💡 **Try it yourself:** add a class attribute `wheels = 4` to a `Car` class and
> confirm two different cars share the same value.

---

## 3. Static and class methods

- A **`@staticmethod`** is a plain function that lives on the class — it doesn't
  take `self` and doesn't touch any object. Good for related utilities.
- A **`@classmethod`** receives the class itself as `cls` (instead of an
  instance), so it can use class attributes or build new instances.

```python
class Temperature:
    @staticmethod
    def c_to_f(celsius):          # no self — just a helper
        return celsius * 9 / 5 + 32

    @classmethod
    def freezing(cls):            # cls is the class itself
        return cls.c_to_f(0)

print(Temperature.c_to_f(100))   # 212.0
print(Temperature.freezing())    # 32.0
```

▶️ **Run it:** `python examples/03_static_and_classmethods.py`

---

## Common mistakes

| Mistake | What happens | Fix |
|---|---|---|
| Changing a class attribute via `self.x = ...` | creates an *instance* attribute that shadows it | Update the shared one with `ClassName.x = ...`. |
| Expecting per-object data in a class attribute | all instances share one value | Set per-object data in `__init__` with `self.`. |
| Adding `self` to a `@staticmethod` | it doesn't get an instance | Drop `self`, or use a normal method. |
| Calling an instance method on the class | missing `self` | Use a `@staticmethod`/`@classmethod`, or make an object. |

---

## Recap / cheat-sheet

```python
class C:
    shared = 0                 # class attribute (shared by all instances)

    def __init__(self, x):
        self.x = x             # instance attribute (per object)
        C.shared += 1          # update the shared one via the class

    @staticmethod
    def helper(a, b):          # no self/cls — a utility
        return a + b

    @classmethod
    def make(cls):             # receives the class as cls
        return cls(0)

C.shared          # read the class attribute
C.helper(1, 2)    # call the static method
```

---

## Exercises

Run a file with `python exercises/<file>.py`, then compare with the matching
file in [`solutions/`](solutions/).

1. [`exercises/01_shared_attribute.py`](exercises/01_shared_attribute.py) — a class attribute shared by instances.
2. [`exercises/02_count_objects.py`](exercises/02_count_objects.py) — count how many objects were made.
3. [`exercises/03_static_method.py`](exercises/03_static_method.py) — write a `@staticmethod`.

> Try each yourself **before** opening the solution.

---

🎉 **That's the final lesson!** Head to the [capstone projects](../../projects/) to
put everything together.
