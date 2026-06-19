"""Instance attributes (per object) vs class attributes (shared).

Run me:  python 01_class_vs_instance.py
"""

class Dog:
    species = "Canis familiaris"    # CLASS attribute — shared by every Dog

    def __init__(self, name):
        self.name = name            # INSTANCE attribute — unique per dog

a = Dog("Rex")
b = Dog("Fido")

print(a.name, b.name)         # Rex Fido                          (different)
print(a.species, b.species)   # Canis familiaris Canis familiaris (shared)
